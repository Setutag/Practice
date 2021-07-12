import numpy as np
import cv2

cap = cv2.VideoCapture(0)

x,y,h,w = 200,0,1000,200


while(cap.isOpened()):
    ret, frame = cap.read()

   
    if ret==True:
       
        crop_frame = frame[y:y+h, x:x+w]
         
        cv2.imshow('frame',frame)
        cv2.imshow('croped',crop_frame)

        if cv2.waitKey(1) == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
