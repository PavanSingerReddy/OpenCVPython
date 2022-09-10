import cv2

img = cv2.imread("Resources/pic1.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Imgae",imgGray)

cv2.waitKey(0)