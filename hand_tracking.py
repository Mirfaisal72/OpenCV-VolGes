import cv2
import numpy as np
import mediapipe as mp
import time
wCam ,hCam = 1280,820
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
ptime = 0

while True:
    ret , frame = cap.read()
    RGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    result = hands.process(RGB)
    print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handmrks in result.multi_hand_landmarks:
            for id,lm in enumerate(handmrks.landmark):
               # print(id,lm) #this prints the x,y coordinate of lamdmarks
                # converting cordinates into pixels
                h, w, c = frame.shape
                pixels_x , pixels_y = int(lm.x *w) , int(lm.y*h) 
                print(id,pixels_x,pixels_y)
                cv2.circle(frame,(pixels_x,pixels_y),10,(0,0,255),cv2.FILLED)
            mpdraw.draw_landmarks(frame,handmrks,mphands.HAND_CONNECTIONS)
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(frame,f"frame Rate: {int(fps)}",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()