#install.packages("jsonlite")
#install.packages("curl")
#install.packages("doParallel")


#setwd("/home/cmelani/Documents/github/ML")
source("busquedaAImagen.R")


library(jsonlite)
library(doParallel)

cl <- makeCluster(20)
registerDoParallel(cl)

local_directory <- "/home/camilo/Documents/ML/Imagenes/"

refreshData=FALSE
termino<-"Auto"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,0,2000,outputDir,refreshData)

refreshData=TRUE
termino<-"Fiat"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,1,400,outputDir,refreshData)

refreshData=TRUE
termino<-"Peugeot"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,1,400,outputDir,refreshData)

refreshData=TRUE
termino<-"Ford"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,1,400,outputDir,refreshData)



items<-c("Climatizacion", "Freezers", "Plantas", "Electrodomesticos", "Planchas","TV","Hornos","Cocinas","Lavarropas","Casa")
for (termino in items){
  print(termino)
  refreshData=TRUE
  outputDir<-paste(local_directory, "imagenes_", termino, sep="")
  if (!file.exists(outputDir)){
    dir.create(file.path(outputDir))
  }  
  busquedaAImagen(termino,0,50,outputDir,refreshData)
}


stopCluster(cl)


