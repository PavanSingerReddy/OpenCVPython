import cv2

img = cv2.imread("Resources/SampleImage.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)    #blur should be in odd numbers like (7,7),(5,5),(3,3)
imgCanny = cv2.Canny(img,100,100)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("canny image",imgCanny)

cv2.waitKey(0)