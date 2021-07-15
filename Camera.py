import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, img = cap.read()
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, np.array([30, 70, 0]), np.array([120, 255, 120]))
	
	moments = cv2.moments(mask, 1)
	
	dM01 = moments['m01']
	dM10 = moments['m10']
	dArea = moments['m00']
	
	x = int(dM10 / dArea)
	y = int(dM01 / dArea)	
	
	cv2.rectangle(img, (220, 140), (420, 340), (255, 255, 255), 2)
	
	if (((x > 220)&(x < 420))&((y > 140)&(y < 340))):
		cv2.putText(img, 'True', (220, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 2)
	else:
		cv2.putText(img, 'False', (220, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 2)
	
	cv2.imshow('Res', img)
	
	if cv2.waitKey(1) == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
	
	
	