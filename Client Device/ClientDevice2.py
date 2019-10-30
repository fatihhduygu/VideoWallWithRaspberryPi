import socket
import cv2
import numpy
import pickle
import zlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


clientIpAddress = socket.gethostbyname(socket.gethostname())
print(clientIpAddress)
host = '192.168.1.37'     #You should enter ip adress of client device
port = 1110
buffer = 460800


# ---- Client Connections -----

s.connect((host, port))
gelenMesaj = b""
message = "Hello"
s.send(message.encode())
while True:
    gelenMesaj += s.recv(buffer)
    if len(gelenMesaj) == (46080 * 20):
        img1 = numpy.fromstring(gelenMesaj, dtype=numpy.uint8)
        print("boyut", len(img1), "resim", img1)
        img1 = img1.reshape(480, 640, 3)


        #cv2.imdecode(img1,cv2.IMREAD_COLOR)
        #cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        
        
        cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.resizeWindow('image', 1080, 1920)
        flow_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        cv2.imshow("image", flow_img)
        cv2.waitKey(1)
        gelenMesaj = b""
        

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break