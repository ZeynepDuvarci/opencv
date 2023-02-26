# 26.02.2023
# it gives error -215:Assertion failed
# because video ran out of frames
# also this error may happen when you given the wrong directory 

import cv2
import numpy as np

# resizing function for videos, live video and images
def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)

capture= cv2.VideoCapture('dog.mp4')
    
while True:
    #read video frame by frame
    isTrue, frame=capture.read()
    
    cv2.imshow('Video',frame)
    
    cv2.imshow('Resized Video',rescaleFrame(frame))
    
    #letter d is pressed video is stops
    if cv2.waitKey(20) & 0xFF==ord('d'):
       break 

capture.relase()
cv2.destroyAllWindows()