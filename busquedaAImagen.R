busquedaAImagen<-function(termino,offset,cantPaginas,destino,refreshData){
  if (refreshData)
  {
    idHist=data.frame(id=c()) 
  }
  else
  {
    idHist <- read.table(paste(local_directory,termino,sep=" "),sep=";")
    names(idHist)<-c("id")
  }
  
  for (i in offset:offset+cantPaginas){
    print(paste("i",i))
    items <- fromJSON(paste("https://api.mercadolibre.com/sites/MLA/search?q=",termino,"&offset=",i,sep=""))
    idf <-data.frame(id=items$results$id)
    for (j in 1:nrow(idf))
    {
      id=idf$id[j]
      if (!(is.element(id, idAutosHist$id)))
      {
        item <- fromJSON(paste("https://api.mercadolibre.com/items/",id,sep=""))
        pictures<-item$pictures
        urls<-item$pictures$url
        ids<-item$pictures$id
        foreach(p=1:length(pictures$url)) %dopar%  
              {
                filename<-paste(destino,"/",pictures$id[p],".jpg",sep="")
                print(filename)
                download.file(pictures$url[p], filename, "auto", quiet = FALSE, mode = "w",cacheOK = TRUE,extra = getOption("download.file.extra"))
              }
      }
      else
      {
        print("repetido")
      }
    }
  idHist<-rbind(idHist,idf)
  idHist <- unique(idHist)
  write.table(idHist,file = paste(local_directory,termimo,"_Hist",sep=" "),sep=";",row.names = FALSE,col.names = FALSE)
  }
}
