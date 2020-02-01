




import cv2
import numpy as np
# import pymouse

from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics



palm = cv2.CascadeClassifier('palm.xml')

fist = cv2.CascadeClassifier('fist.xml')

gestures = cv2.CascadeClassifier('gestures.xml')

mouse = Controller()

original_width = GetSystemMetrics(0)
original_height = GetSystemMetrics(0)


cap = cv2.VideoCapture(0)

width  = cap.get(3)
height = cap.get(4)

print(width, height)

while True:
    ret, img =cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    palm_cascade = palm.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in palm_cascade:
        cv2.rectangle(img , (x,y) , ((x+w),(y+h)), (255,0,0), 2)

     
    fist_cascade = fist.detectMultiScale(gray,1.3,5)
    for(xf,yf,wf,hf) in fist_cascade:
        cv2.rectangle(img , (xf,yf) , ((xf+wf),(yf+hf)), (0,255,0), 2)
        center_x = (xf + xf + wf) // 2
        center_y = (yf + yf + hf) // 2
        cv2.rectangle(img , (center_x - 5, center_y - 5) , ((center_x + 5), (center_y + 5)), (255,0,0), -1)
        img[center_x, center_y] = (255, 0, 0)
        mouse.move(xf-250, yf-250)
        
    
    
    # cv2.namedWindow("img",cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("img",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.putText(img, "Hello Archit !", (20, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, 1, 1, 100000)
    cv2.imshow('img',img)
     
    k = cv2.waitKey(30) & 0xff
     
    if k == 27:
        break      
    
cap.release()
cv2.destroyAllWindows() 