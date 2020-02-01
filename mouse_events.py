




import cv2
import numpy as np
# import pymouse

from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics
from utils import findActualRect, findActualRectWidth, convertAct



palm = cv2.CascadeClassifier('cascade_classifiers/palm.xml')

fist = cv2.CascadeClassifier('cascade_classifiers/fist.xml')

fingertip = cv2.CascadeClassifier('cascade_classifiers/fingertip.xml')

mouse = Controller()

original_width = GetSystemMetrics(0)
original_height = GetSystemMetrics(1)

cap = cv2.VideoCapture(0)

video_width  = cap.get(3)
video_height = cap.get(4)
width = original_width // 4
height = original_height // 4
clicked = False
while True:
    ret, img =cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
    palm_cascade = palm.detectMultiScale(gray, 1.3, 5)
    if clicked == False:    
        for(x,y,w,h) in palm_cascade:
            cv2.rectangle(img , (x,y) , ((x+w),(y+h)), (0,0,255), 2)
            mouse.press(Button.left)
            mouse.release(Button.left)
            clicked = True


     
    fist_cascade = fist.detectMultiScale(gray,1.3,5)
    for(xf,yf,wf,hf) in fist_cascade:
        clicked = False
        cv2.rectangle(img , (xf,yf) , ((xf+wf),(yf+hf)), (0,255,0), 2)

        # Marking the center of the fist
        center_x = (xf + xf + wf) // 2
        center_y = (yf + yf + hf) // 2
        cv2.rectangle(img , (center_x - 5, center_y - 5) , ((center_x + 5), (center_y + 5)), (255,0,0), -1)
        try:
            ## Coloring the actual mid
            img[center_x, center_y] = (255, 0, 0)
            center_x = center_x * 4
            center_y = center_y * 4

            mouse.position = (center_x - 450, center_y - 450)
            # mouse.move(xf, yf)
        except:
            pass
        
        
    
    
    img = cv2.resize(img, (width, height), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
    cv2.putText(img, "Hello Archit !", (20, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, 1, 1, 100000)
    cv2.imshow('img', img)
    cv2.moveWindow('img', 1000, 500)
     
    k = cv2.waitKey(30) & 0xff
     
    if k == 27:
        break      
    
cap.release()
cv2.destroyAllWindows() 