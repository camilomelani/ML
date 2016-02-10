#install.packages("jsonlite")
#install.packages("curl")
#install.packages("doParallel")


setwd("/home/cmelani/Documents/github/ML")
source("busquedaAImagen.R")



library(jsonlite)
library(doParallel)

cl <- makeCluster(40)
registerDoParallel(cl)

home<-Sys.getenv("HOME")
local_directory <- paste(home,"/Documents/github/ML/",sep="")

refreshData=TRUE
termino<-"Auto"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,0,500,outputDir,refreshData)
                
refreshData=TRUE
termino<-"Flores"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,0,5,outputDir,refreshData)
                

refreshData=TRUE
termino<-"Casas"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,0,5,outputDir,refreshData)


stopCluster(cl)


