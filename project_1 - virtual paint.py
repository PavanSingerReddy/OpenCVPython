import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)


myColors = [[88,102,58,255,159,255]]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        cv2.imshow(str(color[0]),mask)

while True:
    success,img = cap.read()
    findColor(img,myColors)
    cv2.imshow("Result",img)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break