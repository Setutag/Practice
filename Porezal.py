import numpy as np
import cv2

cap = cv2.VideoCapture(0)

x,y,h,w = 200,0,1000,200


while(cap.isOpened()):
   _, img_curr, ret, frame = cap.read()

   		hsv = cv2.cvtColor(img_curr, cv2.COLOR_BGR2HSV)
	
		ld = np.array([0, 120, 170])
		ud = np.array([10, 255, 255])
		lmask = cv2.inRange(hsv, ld, ud)
		ld = np.array([170, 120, 170])
		ud = np.array([180, 255, 255])
		umask = cv2.inRange(hsv, ld, ud)
		mask = lmask + umask
    if ret==True:
       
        crop_frame = frame[y:y+h, x:x+w]

         
        cv2.imshow('frame',frame)
        cv2.imshow('croped',crop_frame)
		cv2.imshow('WEB_HSV', mask)

        if cv2.waitKey(1) == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()