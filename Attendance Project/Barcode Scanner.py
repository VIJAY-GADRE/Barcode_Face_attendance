import numpy as np
import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture("http://192.168.1.2:8080/video")
cam.set(3, 640)
cam.set(4, 480)

with open('BarcodeImagesData/myDataFile') as file:
    myBarDataList = file.read().splitlines()
print(myBarDataList)

while True:
    success, img = cam.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myBarDataList:
            print("Un-Authorized")
        else:
            print("Authorized")

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))

        cv2.polylines(img, [pts], True, (0, 255, 0), 4)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Barcode Video", img)
    cv2.waitKey(1)