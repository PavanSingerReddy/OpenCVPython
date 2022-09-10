import cv2
import numpy as np

img = cv2.imread("Resources/SampleImage.jpg")
kernal = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)    #blur should be in odd numbers like (7,7),(5,5),(3,3)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)  #useful for detecting disconnected edges
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)  #it is used to thin the edges.This does opposite of image Dialation

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Imgae",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)