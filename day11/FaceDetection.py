import cv2
import mediapipe as mp
import time

cap =cv2.VideoCapture('day11/video.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('day11/video.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
faceDetection=mpFaceDetection.FaceDetection()

while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results= faceDetection.process(imgRGB)
    
    if results.detections:
        for id,detection in enumerate(results.detections):
            bboxC=detection.location_data.relative_bounding_box
            ih, iw, ic=img.shape
            
            bbox=int(bboxC.xmin*iw), int(bboxC.ymin*ih), \
                int(bboxC.width*iw),int(bboxC.height*ih)
            
            cv2.rectangle(img,bbox,(255,0,255),2)    
            
    result.write(img)        
    cv2.imshow('Image',img)
    cv2.waitKey(1)
result.release()