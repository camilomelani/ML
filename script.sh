#!/bin/bash

#find ML_ClasificadasBN/imagenes_Auto -iname "*.jpg" -exec echo \{\} \; >> cars.info
#/home/camilo/Documents/ML/

#find ML_ClasificadasBN/ -iname "*copy*" -exec ls \{\}  \; 
#http://abhishek4273.com/2014/03/16/traincascade-and-car-detection-using-opencv/
#http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html
#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
#PATH=$PATH:/home/ubuntu/OpenCV/OpenCV/build/bin/
#export PATH
#ls imagenes_Ford_Frontal/*.jpg | xargs -r -I FILE   convert FILE -verbose -colorspace Gray FILE


entranarClasificador()
{
   declare -a DirPositivas=("${!1}")
   declare -a DirNegativas=("${!2}")
   declare -a DirOutput=($3)

   echo "Imagenes positivas" "${DirPositivas[@]}"
   echo "Imagenes Negativas" "${DirNegativas[@]}"
   echo "Directoriod de salida" $DirOutput

   rm positivas.info
   rm positivas1.tmp
   rm positivas2.tmp
   touch positivas1.tmp


   for d in "${DirPositivas[@]}"
   do
	find $d -iname "*.jpg" -exec identify \{\}   \; | cut -d' ' -f1,3 >> positivas1.tmp
   done
   sed 's/ / 1 0 0 /g' positivas1.tmp > positivas2.tmp
   sed 's/x/ /g' positivas2.tmp > positivas.info
   var=`cat positivas.info | wc -l`
   var=$(echo "scale=0;0.9*$var" |bc)
   CantImagenesPositivas=$(echo "$var/1" | bc )

#opencv_createsamples
   opencv_createsamples -info positivas.info -num $CantImagenesPositivas -w 48 -h 24 -vec positivas.vec

   rm negativas.txt
   touch negativas.txt

   for d in "${DirNegativas[@]}"
   do
      find $d -iname "*.jpg" >> negativas.txt
   done


   CantImagenesNegativas=`cat NoCars.txt | wc -l`

   rm -fr $DirOutput
   mkdir $DirOutput

   opencv_traincascade -data $DirOutput -vec positivas.vec -bg negativas.txt -numStages 10 -nsplits 2 -minhitrate 0.999 -maxfalsealarm 0.5 -numPos $CantImagenesPositivas -numNeg $CantImagenesNegativas -w 48 -h 24 
}


#Auto Exterior vs No Auto + Interior
positivas=(
	"ML_ClasificadasBN/imagenes_Auto_Atras"
	"ML_ClasificadasBN/imagenes_Auto_Frontal"
        "ML_ClasificadasBN/imagenes_Auto_Frente"
        "ML_ClasificadasBN/imagenes_Auto_Costado"
	)

negativas=(
        "ML_ClasificadasBN/imagenes_Auto"
        "ML_ClasificadasBN/imagenes_Casa"
        "ML_ClasificadasBN/imagenes_Climatizacion"
        "ML_ClasificadasBN/imagenes_Cocinas"
        "ML_ClasificadasBN/imagenes_Electrodomesticos"
        "ML_ClasificadasBN/imagenes_Freezers"
        "ML_ClasificadasBN/imagenes_Hornos"
        "ML_ClasificadasBN/imagenes_Lavarropas"
        "ML_ClasificadasBN/imagenes_Planchas"
        "ML_ClasificadasBN/imagenes_Plantas"
        "ML_ClasificadasBN/imagenes_TV"
    )
entranarClasificador positivas[@] negativas[@] "AutoExterior" 

#Auto Frente vs Auto Exterior - Auto Frente
positivas=(
        "ML_ClasificadasBN/imagenes_Auto_Frente"
	)
negativas=(
        "ML_ClasificadasBN/imagenes_Auto_Costado"
	"ML_ClasificadasBN/imagenes_Auto_Atras"
	"ML_ClasificadasBN/imagenes_Auto_Frontal"
    )
entranarClasificador positivas[@] negativas[@] "AutoFrente" 

#   Auto Frontal vs Auto Exterior - Auto Frontal
positivas=(
	"ML_ClasificadasBN/imagenes_Auto_Frontal"
	)
negativas=(
        "ML_ClasificadasBN/imagenes_Auto_Costado"
	"ML_ClasificadasBN/imagenes_Auto_Atras"
        "ML_ClasificadasBN/imagenes_Auto_Frente"
    )
entranarClasificador positivas[@] negativas[@] "AutoFrontal" 



#   Auto Costado vs Auto Exterios - Auto Costado
positivas=(
        "ML_ClasificadasBN/imagenes_Auto_Costado"
	)
negativas=(
	"ML_ClasificadasBN/imagenes_Auto_Frontal"
	"ML_ClasificadasBN/imagenes_Auto_Atras"
        "ML_ClasificadasBN/imagenes_Auto_Frente"
    )
entranarClasificador positivas[@] negativas[@] "AutoCostado" 

#   Auto Atras vs Auto Exterior - Auto Atras
positivas=(
	"ML_ClasificadasBN/imagenes_Auto_Atras"
	)
negativas=(
        "ML_ClasificadasBN/imagenes_Auto_Costado"
	"ML_ClasificadasBN/imagenes_Auto_Frontal"
        "ML_ClasificadasBN/imagenes_Auto_Frente"
    )
entranarClasificador positivas[@] negativas[@] "AutoAtras" 


#   Auto interior vs No auto
positivas=(
        "ML_ClasificadasBN/imagenes_Auto"
	)
negativas=(
        "ML_ClasificadasBN/imagenes_Casa"
        "ML_ClasificadasBN/imagenes_Climatizacion"
        "ML_ClasificadasBN/imagenes_Cocinas"
        "ML_ClasificadasBN/imagenes_Electrodomesticos"
        "ML_ClasificadasBN/imagenes_Freezers"
        "ML_ClasificadasBN/imagenes_Hornos"
        "ML_ClasificadasBN/imagenes_Lavarropas"
        "ML_ClasificadasBN/imagenes_Planchas"
        "ML_ClasificadasBN/imagenes_Plantas"
        "ML_ClasificadasBN/imagenes_TV"
    )
entranarClasificador positivas[@] negativas[@] "InteriorAuto" 




