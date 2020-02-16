from subprocess import call
import win32api
import struct
import sys
import json


def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)


def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}


def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()


def send(encodedMessage):
    sendMessage(encodeMessage(encodedMessage))

count_mesage = 0
while True:
    receivedMessage = getMessage()
    host = ""
    id = ""
    if "host" in receivedMessage:
        host = receivedMessage["host"]
    if "id" in receivedMessage:
        id = receivedMessage["id"]
    count_mesage += 1
    response = {}
    if receivedMessage["message"] == "exit":
        break
    if receivedMessage["message"] == "1":
        win32api.MessageBox(0, 'RUN', 'title')
    if receivedMessage["message"] == "notepad":
        call(["notepad.exe"])
    if receivedMessage["message"] == "calc":
        call(["calc.exe"])
        response["eval"] = "alert('Message From Python')"  #  Запуск JS кода
    if "cmd" in receivedMessage:
        response["shell"] = call(receivedMessage["cmd"]) # не работает
    response["response"] = count_mesage
    response["host"] = host
    response["id"] = id
    send(response)
