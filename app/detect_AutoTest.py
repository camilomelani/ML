#!/usr/bin/python

#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
#http://mark-kay.net/2014/06/24/detecting-vehicles-cctv-image/
import numpy as np
import cv2
import sys
from datetime import datetime
import datetime
import os,glob


def Nivel(nivel,imagenO,output):
	detect=0
	vehicle_classifier_Costado = cv2.CascadeClassifier("Costado.xml")
	vehicle_classifier_Frente = cv2.CascadeClassifier("Frente.xml")
	vehicle_classifier_Frontal = cv2.CascadeClassifier("Frontal.xml")
	vehicle_classifier_Atras = cv2.CascadeClassifier("Atras.xml")
	vehicle_classifier_Exterior = cv2.CascadeClassifier("Exterior.xml")

	W = 100.0
   	height, width = imagenO.shape
   	imgScale = W/width
   	newX,newY = imagenO.shape[1]*imgScale, imagen.shape[0]*imgScale
   	imagen = cv2.resize(imagenO,(int(newX),int(newY)))
	
    	height, width = imagen.shape
	minSize=(int(width*0.25),int(height*0.25))
	maxSize=(int(width*1.00),int(height*1.00))

	minSize=(int(width*0.15),int(height*0.15))
	maxSize=(int(width*1.00),int(height*1.00))
	autos1 = vehicle_classifier_Costado.detectMultiScale(image=imagen, scaleFactor=1.04, minNeighbors=20, minSize=minSize,maxSize=maxSize)

	minSize=(int(width*0.25),int(height*0.25))
	maxSize=(int(width*1.00),int(height*1.00))
        autos2 = vehicle_classifier_Frente.detectMultiScale(image=imagen, scaleFactor=1.01, minNeighbors=20, minSize=minSize,maxSize=maxSize)


	minSize=(int(width*0.25),int(height*0.25))
	maxSize=(int(width*1.00),int(height*1.00))
        autos3 = vehicle_classifier_Frontal.detectMultiScale(image=imagen, scaleFactor=1.1, minNeighbors=20, minSize=minSize,maxSize=maxSize)


	minSize=(int(width*0.35),int(height*0.35))
	maxSize=(int(width*1.00),int(height*1.00))
        autos4 = vehicle_classifier_Atras.detectMultiScale(image=imagen, scaleFactor=1.05, minNeighbors=20, minSize=minSize,maxSize=maxSize)


        autos5 = vehicle_classifier_Exterior.detectMultiScale(image=imagen, scaleFactor=1.05, minNeighbors=20, minSize=minSize,maxSize=maxSize)
	

	if (nivel == 1):
		if (len(autos1) > 0 or len(autos2) > 0 or len(autos3) > 0 or len(autos4) > 0 or len(autos5) > 0):
			resultado = "auto"
		else: 
			resultado = "no_auto"
	elif (nivel == 2):
		if (not(len(autos1) > 0 or len(autos2) > 0 or len(autos3) > 0 or len(autos4) > 0)):
			resultado = "no_auto"
		else:
			if (len(autos3) > 0):
				resultado = "auto_angular_frontal"
			else:
				resultado = "auto_no_angular_frontal"
				
	elif (nivel == 3):
		if (not(len(autos1) > 0 or len(autos2) > 0 or len(autos3) > 0 or len(autos4) > 0)):
			resultado = "no_auto"
		else:
			if (len(autos3) > 0):
				resultado = "auto_angular_frontal"
			elif (len(autos2)>0):
				resultado = "auto_frente"
			elif (len(autos1)>0):
				resultado = "auto_costado"
			elif (len(autos4)>0):
				resultado = "auto_otra"

	b = datetime.datetime.now()
	return resultado,(b-a)


def classificarDirectorioAuto(inputDir):
	detect = 0
	nodetect = 0
	for filename in glob.glob(os.path.join(inputDir, '*.jpg')):
	   	
		imagen = cv2.imread(filename,0)
		result,tiempo = Nivel(1,imagen,"/tmp/1.jpg")
		if  (str(result) is 'auto'):
			detect = detect + 1
		else:
			nodetect = nodetect + 1

	print 'detect: %d\tnodetect: %d\t %d\t %.02f\t %10s' % (detect,nodetect,detect+nodetect,float(detect)/(detect+nodetect), inputDir)
	return 1	    


def classificarDirectorio(classificador,inputDir):

	vehicle_classifier = cv2.CascadeClassifier(classificador)

	detect = 0
	nodetect = 0
	for filename in glob.glob(os.path.join(inputDir, '*.jpg')):
	   	
		imagen = cv2.imread(filename,0)

		W = 100.0
	   	height, width = imagen.shape
	   	imgScale = W/width
	   	newX,newY = imagen.shape[1]*imgScale, imagen.shape[0]*imgScale
	   	newimg = cv2.resize(imagen,(int(newX),int(newY)))

	    	height, width = newimg.shape
		minSize=(int(width*0.15),int(height*0.15))
		maxSize=(int(width*1.00),int(height*1.00))
	#	autos = vehicle_classifier.detectMultiScale(imagen, 3, 5,minSize=minSize,maxSize=maxSize)
		autos = vehicle_classifier.detectMultiScale(image=newimg, scaleFactor=1.05, minNeighbors=20, minSize=minSize,maxSize=maxSize)
		if (len(autos) == 0):
			nodetect = nodetect + 1
		else:
			detect = detect + 1

	print 'detect: %d\tnodetect: %d\t %d\t %.02f\t %s\t %10s' % (detect,nodetect,detect+nodetect,float(detect)/(detect+nodetect),classificador, inputDir)
	return 1	    









if __name__ == "__main__":
   classificador = sys.argv[1]
   inputDir = sys.argv[2]

   classificarDirectorio(classificador,inputDir)





