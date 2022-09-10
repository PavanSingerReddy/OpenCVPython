import cv2

cap = cv2.VideoCapture("Resources/SampleVideo.mp4")


while True :
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(10) & 0xFF   ==ord('q'):
        break

