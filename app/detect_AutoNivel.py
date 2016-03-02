#!/usr/bin/python

import numpy as np
import cv2
import sys
import datetime
import os
import urllib
import getopt
import sys
#sys.stdout = sys.stderr

def Nivel1(imagen,output):
	detect=0
	vehicle_classifier_Costado = cv2.CascadeClassifier("ML/AutoCostado/cascade.xml")
	vehicle_classifier_Frente = cv2.CascadeClassifier("ML/AutoFrente/cascade.xml")
	vehicle_classifier_Frontal = cv2.CascadeClassifier("ML/AutoFrontal/cascade.xml")
	vehicle_classifier_Atras = cv2.CascadeClassifier("ML/AutoAtras/cascade.xml")

    	height, width = imagen.shape
	minSize=(width/4,height/4)
	maxSize=(width,height)
	a = datetime.datetime.now()
	autos1 = vehicle_classifier_Costado.detectMultiScale(imagen, 3, 5,minSize=minSize,maxSize=maxSize)
        autos2 = vehicle_classifier_Frente.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
        autos3 = vehicle_classifier_Frontal.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
        autos4 = vehicle_classifier_Atras.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
	b = datetime.datetime.now()
	
	imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

	print ("Autos:" + str(str(autos1) + str(autos2) + str(autos3) + str(autos4)))
	print ("...............")

        for (x,y,w,h) in autos1:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),14)
        for (x,y,w,h) in autos2:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,255),14)
        for (x,y,w,h) in autos3:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,255,128),14)
        for (x,y,w,h) in autos4:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,255,0),14)

	cv2.imwrite(output,imagen)
	return 1



def Nivel2(imagen,output):
	detect=0
	vehicle_classifier_Costado = cv2.CascadeClassifier("ML/AutoCostado/cascade.xml")
	vehicle_classifier_Frente = cv2.CascadeClassifier("ML/AutoFrente/cascade.xml")
	vehicle_classifier_Frontal = cv2.CascadeClassifier("ML/AutoFrontal/cascade.xml")
	vehicle_classifier_Atras = cv2.CascadeClassifier("ML/AutoAtras/cascade.xml")

    	height, width = imagen.shape
	minSize=(width/4,height/4)
	maxSize=(width,height)
	a = datetime.datetime.now()
	autos1 = vehicle_classifier_Costado.detectMultiScale(imagen, 3, 5,minSize=minSize,maxSize=maxSize)
        autos2 = vehicle_classifier_Frente.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
        autos3 = vehicle_classifier_Frontal.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
        autos4 = vehicle_classifier_Atras.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
	b = datetime.datetime.now()
	
	imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)


	print ("Auto:" + str(str(autos1) + str(autos2) + str(autos4))) 
	print ("Frontal:" + str(autos3))

        for (x,y,w,h) in autos1:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,255,0),14)
        for (x,y,w,h) in autos2:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,255),14)
        for (x,y,w,h) in autos3:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,255,128),14)
        for (x,y,w,h) in autos4:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,255,0),14)

	cv2.imwrite(output,imagen)
	return 1

def Nivel3(imagen,output):
	detect=0
#this is the cascade we just made. Call what you want
	vehicle_classifier_Costado = cv2.CascadeClassifier("ML/AutoCostado/cascade.xml")
	vehicle_classifier_Frente = cv2.CascadeClassifier("ML/AutoFrente/cascade.xml")
	vehicle_classifier_Frontal = cv2.CascadeClassifier("ML/AutoFrontal/cascade.xml")
	vehicle_classifier_Atras = cv2.CascadeClassifier("ML/AutoAtras/cascade.xml")

    	height, width = imagen.shape
	minSize=(width/4,height/4)
	maxSize=(width,height)
	a = datetime.datetime.now()
	autos1 = vehicle_classifier_Costado.detectMultiScale(imagen, 3, 5,minSize=minSize,maxSize=maxSize)
        autos2 = vehicle_classifier_Frente.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
        autos3 = vehicle_classifier_Frontal.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
        autos4 = vehicle_classifier_Atras.detectMultiScale(imagen, 3, 5, minSize=minSize,maxSize=maxSize)
	b = datetime.datetime.now()
	
	imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
	print ("Costado:" + str(autos1))
	print ("Frente:" + str(autos2))
	print ("Frontal:" + str(autos3))
	print ("Atras:" + str(autos4))

        for (x,y,w,h) in autos1:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,255,0),14)
        for (x,y,w,h) in autos2:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,255),14)
        for (x,y,w,h) in autos3:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,255,128),14)
        for (x,y,w,h) in autos4:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(128,255,0),14)

	cv2.imwrite(output,imagen)
	return 1



def main(argv):
   nivel = 0
   url = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"n:u:o:",["nivel=","url=","output="])
   except getopt.GetoptError:
      print 'detect_AutoNivel.py -n nivel -u url -o outputfile'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'detect_AutoNivel.py -n nivel -i url -o outputfile'
         sys.exit()
      elif opt in ("-n", "--nivel"):
         nivel = arg
      elif opt in ("-u", "--url"):
         url = arg
      elif opt in ("-o", "--output"):
         outputfile = arg

   
   #Download file
   tmpfile="/var/www/html/imagenes_entrada/" + url.split('/')[-1]
   urllib.urlretrieve(url, tmpfile)

   #Leo imagen
   imagen = cv2.imread(tmpfile,0)
   #Resize a 1024
   W = 500.0
   height, width = imagen.shape
   imgScale = W/width
   newX,newY = imagen.shape[1]*imgScale, imagen.shape[0]*imgScale
   newimg = cv2.resize(imagen,(int(newX),int(newY)))

   if (nivel=="1"):
	return Nivel1(newimg,outputfile)
   elif (nivel=="2"):
	return Nivel2(newimg,outputfile)
   elif (nivel=="3"):
	return Nivel3(newimg,outputfile)


if __name__ == "__main__":
   main(sys.argv[1:])


