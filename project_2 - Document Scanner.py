import cv2
import numpy as np

###########################
widthImg = 640
heightImg = 480
###########################

cap =  cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,130)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernal = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernal,iterations=2)
    imgThreshold = cv2.erode(imgDial,kernal,iterations=1)      #eroding the dialated image

    return imgThreshold

def getContours(img):
    biggest =  np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if area >5000:
            cv2.drawContours(imgCountours,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.03*peri,True)
            if area > maxArea and len(approx) ==4:
                biggest = approx
                maxArea = area
    return biggest

while True:
    success , img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgCountours = img.copy()
    imgThreshold = preProcessing(img)
    getContours(imgThreshold)
    cv2.imshow("Result",imgCountours)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break