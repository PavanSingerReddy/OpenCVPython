import cv2
import numpy as np

def empty(a):
    pass



path = "Resources/cars.jpeg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)



img = cv2.imread(path)


imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow("Original",img)

cv2.imshow("HSV",imgHSV)

cv2.waitKey(0)