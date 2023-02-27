# 27.02.2023

import cv2
import numpy as np

# 0 your pc camera
# 1 USB camera
# 2 video or direction
haar_cascade=cv2.CascadeClassifier('haar_face.xml')

camera=cv2.VideoCapture(0)

frame_width = int(camera.get(3))
frame_height = int(camera.get(4))
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('video.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while True:
    ret,img=camera.read()
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    
    for (x,y,w,h) in faces_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

    img=cv2.flip(img,1)
    
    result.write(img)
    
    cv2.imshow('Video',img)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
camera.release()
result.release()

cv2.destroyAllWindows()
