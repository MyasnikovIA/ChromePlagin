((window, browser) => {
    const hostName = "com.google.chrome.example.echo";
    window.browser = browser;
    browser.runtime.onConnect.addListener(function (scriptPort) {
        var hostPort = browser.runtime.connectNative(hostName);
        scriptPort.onMessage.addListener(function (message) {
            hostPort.postMessage(message);
        });
        scriptPort.onDisconnect.addListener(function () {
            hostPort.disconnect();
        });
        hostPort.onMessage.addListener(function (message) {
            scriptPort.postMessage(message);
        });
        hostPort.onDisconnect.addListener(function () {
            if (browser.runtime.lastError) {
                scriptPort.postMessage({host: hostName, error: "Disconnected: " + browser.runtime.lastError.message});
            } else {
                scriptPort.postMessage({host: hostName, error: "Disconnected"});
            }
            scriptPort.disconnect();
        });
    });
})(window, window.chrome ? chrome : browser);
