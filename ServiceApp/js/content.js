((window, browser) => {
    const hostName = "com.google.chrome.example.echo";
    console.info("Add BarsPy object");
    var port1 = null;
    window.addEventListener("message", (event) => {
        if (port1 == null) {
            port1 = browser.runtime.connect(browser.runtime.id);
            port1.onMessage.addListener(function (response) {
                if (response['host'] == hostName) {
                    // обработка двунаправленных сообщений между Python и JavaScript
                    if (response['eval'] != undefined) {
                        eval('' + response['eval']);
                        delete response['eval'];
                    }
                    response['MessageToPlagin'] = 1
                    window.postMessage(response, '*')
                }
            });
            port1.onDisconnect.addListener(() => {
                if (port1.error) {
                    console.info("Error", port1.error);
                    return;
                }
                console.info("Disconnected");
            });
        }
        if ((event.source == window)
            && (event.data != undefined)
            && (event.data['host'] == hostName)
            && (event.data['MessageToPlagin'] == undefined)
            && (event.data['MessageToPython'] != undefined)
        ) {
            if (port1 != null) {
                delete event.data['MessageToPython']
                try{
                   port1.postMessage(event.data); // отправка сообщения в Python из JavaScript
                }catch(err) {
                   port1 = null;
                   console.log("Error:",err.message);
                }
                if (event.data["message"] == "exit") {
                    port1 = null;
                }
            }
        }
    });


    function includeScript(path) {
        return new Promise((resolve, reject) => {
            var req = new XMLHttpRequest();
            req.onreadystatechange = function () {
                if (req.readyState == 4) {
                    if (req.status >= 200 && req.status < 300) {
                        resolve(req.responseText);
                    } else {
                        reject(req);
                    }
                }
            };
            req.open("GET", browser.extension.getURL(path));
            req.send();
        });
    }

    function injectScript(text) {
        var s = document.createElement('script');
        s.appendChild(document.createTextNode(text));
        s.onload = function () {
            this.parentNode.removeChild(this);
        };
        (document.head || document.documentElement).appendChild(s);
    }


    includeScript("js/adapter.js")
        .then((script) => {
            injectScript("" +
                "(function() {" +
                "  const host = '" + hostName + "';" +
                script +
                "  window['BarsPy'] = new BarsPyAdapter(host);" +
                "})()");
        })
        .catch((error) => {
            console.warn("Could not initialize \"BARS Browser Python Adapter\" extension", error);
        })

})(window, window.chrome ? chrome : browser);