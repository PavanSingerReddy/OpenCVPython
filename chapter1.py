import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350

pts1 = np.float32([[498,447],[1407,351],[666,1743],[1647,1557]])        #actual dimensions of the single card in the entire image use gimp editor to get the dimensions
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])          #resized dimension or wrap dimension points
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("Cards image",imgOutput)


cv2.waitKey(0)