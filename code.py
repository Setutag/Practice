import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, img_curr = cap.read()
	
	hsv = cv2.cvtColor(img_curr, cv2.COLOR_BGR2HSV)
	
	ld = np.array([0, 120, 170])
	ud = np.array([10, 255, 255])
	lmask = cv2.inRange(hsv, ld, ud)
	ld = np.array([170, 120, 170])
	ud = np.array([180, 255, 255])
	umask = cv2.inRange(hsv, ld, ud)
	mask = lmask + umask
	
	
	cv2.imshow('WEB_CURR', img_curr)
	cv2.imshow('WEB_HSV', mask)
	
	key = cv2.waitKey(1)
	if key == 27: # 'Esc' button
		break

cap.release()
cv2.destroyAllWindows()
	