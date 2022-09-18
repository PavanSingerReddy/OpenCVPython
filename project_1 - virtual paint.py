import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)


myColors = [[88,102,58,255,159,255]]

myColorValues = [[255,0,0]]         #BGR

myPoints = []        #[x,y,ColorId]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        if x!=0 and y!=0:
            cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
            newPoints.append([x,y,count])
            count +=1
        # cv2.imshow(str(color[0]),mask)
    return newPoints


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,width,height = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult,cnt,-1,(255.0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.03*peri,True)
            x,y,width,height = cv2.boundingRect(approx)
    return x+(width//2),y


def drawOnCanvas(myPoints,myColorValues) :
    for point in myPoints :
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)  #point[0] is x value point[1] is y value and point[2] is colorId value

while True:
    success,img = cap.read()
    imgResult = img.copy()
    newPoints =  findColor(img,myColors)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break