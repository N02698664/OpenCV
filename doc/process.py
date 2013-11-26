import os
import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_casacde = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('/home/pi/OpenCV/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 100)
	eyes_in_face = img[y:y+h, x:x+w]
	gray_eyes_in_face = img[y:y+h, x:x+w]
	eyes = eyes_cascade.detectMultiScale(gray_eyes_in_face)
	for (ex, ey, ew, eh) in eyes:
		img = cv2.rectangle(eyes_in_face, (ex,ey), (ex+ew,ey+eh), (0,255,0), 100)

cv2.imwrite('/home/pi/OpenCV/test_processed.jpg', img)
