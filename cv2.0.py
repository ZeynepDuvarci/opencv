# 27.02.2023

import cv2

img=cv2.imread('person.jpg')

img0=cv2.imread('people.jpg')


# gray scailing
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray0=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)


haar_cascade=cv2.CascadeClassifier('haar_face.xml')

# minNeighbors is determining the sensitivity
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
faces_rect0=haar_cascade.detectMultiScale(gray0,scaleFactor=1.1,minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')
print(f'Number of faces found = {len(faces_rect0)}')

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
for (x,y,w,h) in faces_rect0:
    cv2.rectangle(img0,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv2.imshow('Detected Faces 1',img)
cv2.imshow('Detected Faces 2',img0)

cv2.waitKey(0)
cv2.destroyAllWindows()