#!/usr/bin/bash

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

    declare -a DirOutput=("${!3}")

    echo "${DirPositivas[@]}"
    echo "${DirNegativas[@]}"
    echo "${DirOutput[@]}"

exit

    rm positivas.info
    touch positivas.info

   for d in "${DirPositivas[@]}"
   do
	find $d -iname "*.jpg" -exec identify \{\}   \; | cut -d' ' -f1,3 >> positivas.info
   done

   sed 's/ / 1 0 0 /g' positivas.info > positivas.info
   sed 's/x/ /g' positivas.info > positivas.info
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
   opencv_traincascade -data $DirOutput -vec cars.vec -bg NoCars.txt \
      -numStages 10 -nsplits 2 -minhitrate 0.999 -maxfalsealarm 0.5 \
      -numPos $CantImagenesPositivas -numNeg $CantImagenesNegativas -w 48 -h 24 
}

   local positivas=(
        "ML_ClasificadasBN/imagenes_Auto_Frente"
        "ML_ClasificadasBN/imagenes_Auto_Costado"
    )

   local negativas=(
        "ML_ClasificadasBN/imagenes_Casa"
        "ML_ClasificadasBN/imagenes_Freezers"
    )


entrenarClasificador positivas[@] negativas[@] data



