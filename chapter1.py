import cv2
import numpy as np

img = cv2.imread("Resources/SampleImage.jpg")


imgHor = np.hstack((img,img,img))


cv2.imshow("Horizontal",imgHor)


cv2.waitKey(0)