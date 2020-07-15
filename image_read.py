import cv2

print('package imported')

file_path = 'image/start_of_new_life.jpg'
img = cv2.imread(file_path)

cv2.imshow("Outout",img)

cv2.waitKey(100)