# 28.02.2023

import numpy as np
import cv2

haar_cascade=cv2.CascadeClassifier('resourcesAndOutputs/haar_face.xml')

people=['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

features=np.load('resourcesAndOutputs/features.npy',allow_pickle=True)
labels=np.load('resourcesAndOutputs/labels.npy',allow_pickle=True)

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('resourcesAndOutputs/face_trained.yml')

img=cv2.imread(r'resourcesAndOutputs/Faces/val/madonna/4.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Person',gray)

faces_rect= haar_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]
    
    label, confidence=face_recognizer.predict(faces_roi)
    print(f'Label: {people[label]} with a confidence of {confidence} ')
    
    cv2.putText(img,str(people[label]),(20,20),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
    
    cv2.putText(img,str('{:.2f}%'.format(confidence)),(20,50),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
    
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=2)

cv2.imshow('Detected Face', img)
cv2.imwrite('madonna.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()