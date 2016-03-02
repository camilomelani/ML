#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
import numpy as np
import cv2

carExterior = cv2.CascadeClassifier('Exterior.xml')
carFrontal = cv2.CascadeClassifier('Frontal.xml')
carAtras = cv2.CascadeClassifier('Atras.xml')
carFrente = cv2.CascadeClassifier('Frente.xml')
carCostado = cv2.CascadeClassifier('Costado.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width = gray.shape
    minSize=(width/4,height/4)
    maxSize=(width,height)
    

    # add this
    # image, reject levels level weights.
    carAExterior = carExterior.detectMultiScale(gray, 10, 10,minSize=minSize,maxSize=maxSize)
    carAFrontal = carFrontal.detectMultiScale(gray, 10, 10,minSize=minSize,maxSize=maxSize)
    carAAtras = carAtras.detectMultiScale(gray, 10, 10,minSize=minSize,maxSize=maxSize)
    carAFrente = carFrente.detectMultiScale(gray, 10, 10,minSize=minSize,maxSize=maxSize)
    carACostado = carCostado.detectMultiScale(gray, 10, 10,minSize=minSize,maxSize=maxSize)

    font = cv2.FONT_HERSHEY_SIMPLEX

    for (x,y,w,h) in carAExterior:
	cv2.putText(img,'Exterior',(x,y), font, 1,(255,255,255),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for (x,y,w,h) in carAFrontal:
	cv2.putText(img,'Frontal',(x,y), font, 1,(255,255,255),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    for (x,y,w,h) in carAAtras:
	cv2.putText(img,'Atras',(x,y), font, 1,(255,255,255),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    for (x,y,w,h) in carAFrente:
	cv2.putText(img,'Frente',(x,y), font, 1,(255,255,255),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,120),2)
    for (x,y,w,h) in carACostado:
	cv2.putText(img,'Costado',(x,y), font, 1,(255,255,255),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,120),2)

#    for (x,y,w,h) in faces:
#        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        
#        roi_gray = gray[y:y+h, x:x+w]
#        roi_color = img[y:y+h, x:x+w]
#        eyes = eye_cascade.detectMultiScale(roi_gray)
#        for (ex,ey,ew,eh) in eyes:
#            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(300) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
