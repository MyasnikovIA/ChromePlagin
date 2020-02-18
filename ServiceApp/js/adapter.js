/*
 * Copyright (c) 2017, BARS Group. All rights reserved.
 */

var globalQueryList = [];

/**
 * BarsPyAdapter
 * Позволяет отправлять\получать сообщения от расширения.
 *
 * @author Myasnikov Ivan Alekcandrovich  based  Vadim Shushlyakov
 */
class BarsPyAdapter {
    constructor(host) {
        this.host = host;
        window.addEventListener('message', function (event) { //приём сообщения
            if (event.data['MessageToPlagin'] != undefined) {
                delete event.data['MessageToPlagin']
                if (event.data["id"] != undefined) {
                    for (let i = 0, n = globalQueryList.length; i < n; i++) {
                        if (globalQueryList[i]['id'] == event.data["id"]) {
                            if (globalQueryList[i]['callback'] != undefined) {
                                if (typeof globalQueryList[i]['callback'] === 'function') {
                                    globalQueryList[i]['callback'](event.data);
                                }
                            }
                            globalQueryList.splice(i, 1);
                            break;
                        }
                    }
                }
            }
        }, false);
    }
    send(action, callbackFunction) {
        var id = this._genId();
        if (callbackFunction == undefined) {
            callbackFunction = null;
        }
        var message = {
            'id': id,
            'message': {"host": this.host, "message": action, "MessageToPython": 1},
            'callback': callbackFunction
        };
        globalQueryList.push(message)
        var loc = '' + window.location;
        window.postMessage({'id': id, "host": this.host, "message": action, "MessageToPython": 1, 'location': loc}, '*')
    }

    /**
     * Возвращает уникальный идентификатор
     * @returns {string}
     */
    _genId() {
        // https://stackoverflow.com/a/2117523
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
            .replace(/[xy]/g, function (c) {
                let r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
                return v.toString(16);
            });
    }
}




