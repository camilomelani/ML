#!/usr/bin/python

#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
#http://mark-kay.net/2014/06/24/detecting-vehicles-cctv-image/
import numpy as np
import cv2
import sys
from datetime import datetime
import datetime

inputfile = sys.argv[1]

#this is the cascade we just made. Call what you want
vehicle_classifier = cv2.CascadeClassifier('data/cascade.xml')

gray = cv2.imread(inputfile,0)
    
a = datetime.datetime.now()
autos = vehicle_classifier.detectMultiScale(gray, 3, 5, maxSize=(600,400),minSize=(300,200))
b = datetime.datetime.now()
print(b-a)

print 'Vehicles detected: %d' % (len(autos))
    
# add this
for (x,y,w,h) in autos:
  cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,0),2)


cv2.imshow('img',gray)

cv2.waitKey(3000)

cv2.destroyAllWindows()
