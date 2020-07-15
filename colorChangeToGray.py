import cv2 
file_path = 'image/start_of_new_life.jpg'
img = cv2.imread(file_path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image",imgGray)

cv2.waitKey(0)