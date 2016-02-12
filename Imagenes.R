#install.packages("jsonlite")
#install.packages("curl")
#install.packages("doParallel")


#setwd("/home/cmelani/Documents/github/ML")
source("busquedaAImagen.R")


library(jsonlite)
library(doParallel)

cl <- makeCluster(20)
registerDoParallel(cl)

home<-Sys.getenv("HOME")
local_directory <- paste(home,"/ML/",sep="")

refreshData=FALSE
termino<-"Auto"
outputDir<-paste(local_directory, "imagenes_", termino, sep="")
dir.create(file.path(outputDir))
busquedaAImagen(termino,0,2000,outputDir,refreshData)
                

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


