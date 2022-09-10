import cv2
import numpy as np

img = cv2.imread("Resources/SampleImage.jpg")
print(img.shape)     #prints the width and height of the image along with its no of channels


imgResize = cv2.resize(img, (300, 150))
print(imgResize.shape)     #prints the width and height of the image along with its no of channels


cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)


cv2.waitKey(0)