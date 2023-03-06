import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands= mp.solutions.hands
hands=mpHands.Hands()
mpDraw =mp.solutions.drawing_utils

toplandmarks=[4,8,12,16,20]

pTime=0
cTime=0

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('day10/video1.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while True:
    success, img= cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    
    # results None or landmark
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                #pixel values
                h, w, c= img.shape
                cx, cy= int(lm.x*w),int(lm.y*h)
                # id: id number of hand points
                print(id,cx,cy)
                
                if id in toplandmarks:
                    cv2.circle(img, (cx,cy), 10, (255,0,255),cv2.FILLED)
                
               
            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
    
    #cTime=time.time()
    #fps=1/(cTime-pTime)
    #pTime=cTime
    
    #cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
    result.write(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

result.release()