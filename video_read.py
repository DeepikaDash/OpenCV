import cv2 
file_path = "image/test.mp4"
cap=cv2.VideoCapture(file_path) 
while True:
    success, img = cap.read()
    cv2.imshow("video" ,img) 
    if (cv2.waitKey(0) & 0xFF ==ord("q")): 
        break