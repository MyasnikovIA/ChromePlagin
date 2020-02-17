from subprocess import call
import win32api
import win32ui
import win32con
import win32print
import struct
import sys
import json
import imgkit
from PIL import Image, ImageWin
import tempfile



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




def print_image(printer_name, encoded_string=None):
    try:
        img = Image.open(encoded_string, 'r')
    except:
        print("error")
        return
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)
    horzres = hdc.GetDeviceCaps(win32con.HORZRES)
    vertres = hdc.GetDeviceCaps(win32con.VERTRES)
    landscape = horzres > vertres
    if landscape:
        if img.size[1] > img.size[0]:
            print('Landscape mode, tall image, rotate bitmap.')
            img = img.rotate(90, expand=True)
    else:
        if img.size[1] < img.size[0]:
            print('Portrait mode, wide image, rotate bitmap.')
            img = img.rotate(90, expand=True)

    img_width = img.size[0]
    img_height = img.size[1]
    if landscape:
        # we want image width to match page width
        ratio = vertres / horzres
        max_width = img_width
        max_height = (int)(img_width * ratio)
    else:
        # we want image height to match page height
        ratio = horzres / vertres
        max_height = img_height
        max_width = (int)(max_height * ratio)
    # map image size to page size
    hdc.SetMapMode(win32con.MM_ISOTROPIC)
    hdc.SetViewportExt((horzres, vertres));
    hdc.SetWindowExt((max_width, max_height))
    # offset image so it is centered horizontally
    offset_x = (int)((max_width - img_width) / 2)
    offset_y = (int)((max_height - img_height) / 2)
    hdc.SetWindowOrg((-offset_x, -offset_y))
    hdc.StartDoc('Result')
    hdc.StartPage()
    dib = ImageWin.Dib(img)
    dib.draw(hdc.GetHandleOutput(), (0, 0, img_width, img_height))
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()


printer_name = win32print.GetDefaultPrinter()
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
        response["eval"] = "alert('Message From Python')"  # Запуск JS кода
    if '[print]' in receivedMessage["message"]:
        my_str = receivedMessage["message"].replace('[print]', '')
        filename = tempfile.mktemp(".png")
        options = {'width': 300, 'height': 100, 'encoding': 'UTF-8', }
        htmlStr = """<!DOCTYPE html> <html> <head><meta charset="utf-8"><title>Тег META, атрибут charset</title></head><body>%s</body></html>""" % my_str
        imgkit.from_string(htmlStr, filename, options=options)
        print_image(printer_name, filename)
        response["eval"] = "alert('OK |%s')" % filename  # Запуск JS кода
    response["response"] = count_mesage
    response["host"] = host
    response["id"] = id
    send(response)
