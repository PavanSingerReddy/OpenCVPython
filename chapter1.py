import cv2
import numpy as np

img = cv2.imread("Resources/SampleImage.jpg")
print(img.shape)     #prints the width and height of the image along with its no of channels


imgResize = cv2.resize(img, (300, 150))
print(imgResize.shape)     #prints the width and height of the image along with its no of channels

imgCropped = img[0:200,100:200]


cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)


cv2.waitKey(0)