#!/usr/bin/python

import numpy as np
import cv2
import sys
from datetime import datetime
import datetime
import os

inputClasificator = sys.argv[1]
inputdir = sys.argv[2]

#this is the cascade we just made. Call what you want
vehicle_classifier = cv2.CascadeClassifier(inputClasificator)
detect = 0
nodetect = 0
outputDir = "imagenes_prueba_resultado/"
for inputfile in os.listdir(inputdir):
	gray = cv2.imread(inputdir + inputfile,0)
    
#	a = datetime.datetime.now()
	autos = vehicle_classifier.detectMultiScale(gray, 3, 5, maxSize=(600,400),minSize=(300,200))
	if len(autos) > 0:
		detect=detect+1
	else:
		nodetect=nodetect+1
        
	imagen = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        for (x,y,w,h) in autos:
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,255,0),14)
	
	print outputDir + inputfile
	cv2.imwrite(outputDir + inputfile,imagen)
#	b = datetime.datetime.now()

print('Objetos detectados: %d Objetos No detectados: %d rate: %.2f' % (detect, nodetect,float(detect)/(detect+nodetect)))
    




