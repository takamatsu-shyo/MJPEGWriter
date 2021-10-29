import cv2

cap = cv2.VideoCapture("http://localhost:7777")
if not(cap.isOpened()):
    print("Failed to open MJPEG streaming")

ret, frame = cap.read()
 
while(True):
    ret, frame = cap.read()
    cv2.imshow("MJPEG Reader", frame)
    cv2.waitKey(1)
