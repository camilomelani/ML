#!/usr/bin/python

#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
#http://mark-kay.net/2014/06/24/detecting-vehicles-cctv-image/
from detect_AutoTest import classificarDirectorioAuto
from detect_AutoTest import classificarDirectorio

clasificadores=[
	"./Exterior.xml"
	]


dir_imagenes=[
	"../ML_ClasificadasBN_2/imagenes_Auto_Frontal_Test", 
	"../ML_ClasificadasBN_2/imagenes_Auto", 
	"../ML_ClasificadasBN_2/imagenes_Auto_Atras_Test", 
	"../ML_ClasificadasBN_2/imagenes_Auto_Costado_Test", 
	"../ML_ClasificadasBN_2/imagenes_Auto_Frente_Test", 
	"../ML_ClasificadasBN_2/imagenes_Bebes", 
	"../ML_ClasificadasBN_2/imagenes_Casa", 
	"../ML_ClasificadasBN_2/imagenes_Climatizacion", 
	"../ML_ClasificadasBN_2/imagenes_Cocinas", 
	"../ML_ClasificadasBN_2/imagenes_Electrodomesticos", 
	"../ML_ClasificadasBN_2/imagenes_Freezers", 
	"../ML_ClasificadasBN_2/imagenes_Hornos", 
	"../ML_ClasificadasBN_2/imagenes_Lavarropas", 
	"../ML_ClasificadasBN_2/imagenes_Microondas", 
	"../ML_ClasificadasBN_2/imagenes_Planchas", 
	"../ML_ClasificadasBN_2/imagenes_Plantas", 
	"../ML_ClasificadasBN_2/imagenes_salud-y-belleza", 
	"../ML_ClasificadasBN_2/imagenes_Tostadora", 
	"../ML_ClasificadasBN_2/imagenes_TV"]





#Para testear classificador individual
for classificador in clasificadores:
  for dir_imagen in dir_imagenes:
     classificarDirectorio(classificador,dir_imagen) 



#for dir_imagen in dir_imagenes:
#     classificarDirectorioAuto(dir_imagen) 







#Para testear classificador completo
#from detect_AutoNivel import classificarDirectorio

#import os
#os.chdir("../")

#for dir_imagen in dir_imagenes:
#  for filename in glob.glob(os.path.join(dir_imagen, '*.jpg')):
#     resultado,tiempo = Nivel(1,filename,"/dev/null")
#     print resultado




