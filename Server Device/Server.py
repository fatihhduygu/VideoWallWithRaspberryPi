import socket
import time
import cv2
import mss
import numpy
import pickle
import zlib
import struct
import tkinter as tk
from time import sleep
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 1110
buffer = 460800
s.bind((host, port))
s.listen(5)


def ekranGonder(baglanti, ipAdress):
    with mss.mss() as sct:
        root = tk.Tk()
        width_px = root.winfo_screenwidth()
        height_px = root.winfo_screenheight()
        print('Width: %i px, Height: %i px' % (width_px, height_px))
        x = int(width_px / 2)
        y = int(height_px / 2)
        monitor = {"top": 0, "left": 0, "width": 480, "height": 640}

        while True:
            img = numpy.array(sct.grab(monitor))
            d = img.flatten()
            t = d.tostring()
            for i in range(20):
                baglanti.send(t[(i) * 46080:(i + 1) * 46080])
            print(ipAdress, "---istemcisine görüntü gonderiliyor---")
            print(baglanti)
            sleep(0.000000001)


def ekranGonder2(baglanti, ipAdress):
    with mss.mss() as sct:
        root = tk.Tk()
        width_px = root.winfo_screenwidth()
        height_px = root.winfo_screenheight()
        print('Width: %i px, Height: %i px' % (width_px, height_px))
        x = int(width_px / 2)
        y = int(height_px / 2)
        monitor2 = {"top": 0, "left": x, "width": 480, "height": 640}

        while True:
            img2 = numpy.array(sct.grab(monitor2))
            d = img2.flatten()
            t = d.tostring()
            # print(len(d))
            # print("Dizi uzunluk:",img)
            for i in range(20):
                baglanti.send(t[(i) * 46080:(i + 1) * 46080])
            print(ipAdress, "---istemcisine görüntü gonderiliyor---")
            print(baglanti)
            sleep(0.000000001)


def ekranGonder3(baglanti, ipAdress):
    with mss.mss() as sct:
        root = tk.Tk()
        width_px = root.winfo_screenwidth()
        height_px = root.winfo_screenheight()
        print('Width: %i px, Height: %i px' % (width_px, height_px))
        x = int(width_px / 2)
        y = int(height_px / 2)
        monitor3 = {"top": 240, "left": 0, "width": 480, "height": 480}

        while True:
            img3 = numpy.array(sct.grab(monitor3))

            d = img3.flatten()
            t = d.tostring()
            for i in range(20):
                baglanti.send(t[(i) * 46080:(i + 1) * 46080])
            print(ipAdress, "---istemcisine görüntü gonderiliyor---")
            print(baglanti)
            sleep(0.000000001)


def ekranGonder4(baglanti, ipAdress):
    with mss.mss() as sct:
        root = tk.Tk()
        width_px = root.winfo_screenwidth()
        height_px = root.winfo_screenheight()
        print('Width: %i px, Height: %i px' % (width_px, height_px))
        x = int(width_px / 2)
        y = int(height_px / 2)
        monitor4 = {"top": 240, "left": x, "width": 480, "height": 480}

        while True:
            img4 = numpy.array(sct.grab(monitor4))
            d = img4.flatten()
            t = d.tostring()
            for i in range(20):
                baglanti.send(t[(i) * 46080:(i + 1) * 46080])
            print(ipAdress, "---istemcisine görüntü onderiliyor---")
            print(baglanti)
            sleep(0.000000001)


def istekAl():
    print('-----Istekler Dinleniyor-----')
    while True:
        baglanti, istemciIpAdress = s.accept()
        istemcidenGelenMesaj = baglanti.recv(buffer)
        print('Istemcinin Mesaji', istemcidenGelenMesaj)
        print('Istemci Ip Adresi :', istemciIpAdress)
        print(type(istemciIpAdress[0]))


        if istemciIpAdress[0] == "192.168.1.36":
            client1 = Thread(target=ekranGonder, args=(baglanti, istemciIpAdress[0]))
            client1.start()

        elif istemciIpAdress[0] == "192.168.1.37":
            client2 = Thread(target=ekranGonder2, args=(baglanti, istemciIpAdress[0]))
            client2.start()

        elif istemciIpAdress[0] == "192.168.1.38":
            client3 = Thread(target=ekranGonder3, args=(baglanti, istemciIpAdress[0]))
            client3.start()

        elif istemciIpAdress[0] == "192.168.1.39":
            client3 = Thread(target=ekranGonder4, args=(baglanti, istemciIpAdress[0]))
            client3.start()


if __name__ == '__main__':
    istekAl()



