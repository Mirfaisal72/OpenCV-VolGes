import cv2
import numpy as np
import mediapipe as mp
import time
import pyautogui
wCam ,hCam = 1280,820
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
ptime = 0
x1=y1=x2=y2 = 0
while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame, 1)
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
                if id == 8:
                    cv2.circle(frame,(pixels_x,pixels_y),15,(0,0,255),cv2.FILLED)
                    x1 = pixels_x
                    y1 = pixels_y
                elif id == 4:                  
                    cv2.circle(frame,(pixels_x,pixels_y),15,(0,0,255),cv2.FILLED)
                    x2 = pixels_x
                    y2 = pixels_y
                else:
                    cv2.circle(frame,(pixels_x,pixels_y),10,(255,0,255),cv2.FILLED)
            distance = (np.sqrt((x2-x1)**2+(y2-y1)**2))//4
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
            mpdraw.draw_landmarks(frame,handmrks,mphands.HAND_CONNECTIONS)
            if(distance > 35):
                pyautogui.press('volumeup')
            else:
                pyautogui.press("volumedown")

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(frame,f"frame Rate: {int(fps)}",(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()