import cv2
import mediapipe as mp
import time

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()

cap=cv2.VideoCapture('day9/pose.mp4')
pTime=0

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('day9/video.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
while True:
    succes, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            print(id, lm)
            cx,cy=int(lm.x*w),int(lm.y*h)
            print(id,cx,cy)
            cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
        
    #cTime=time.time()
    #fps=1/(cTime-pTime)
    #pTime=cTime
    
    
    result.write(img)
    #cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))
    cv2.imshow("Image",img)
    cv2.waitKey(20)
    
result.release()