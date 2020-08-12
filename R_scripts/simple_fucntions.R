add2 <- function(x,y) {
  x+y ### sume dos valores
}
above10 <- function (x){
  use <- x > 10 ### este es un vector logico
  x[use] ### el valor que quieres regresar
}

above <- function (x,n){
  use <- x < n
  x[use]
}

columnmean <- function (x){ # x es un archivo con columnas
  number_columns <- ncol(x) # cuanta las columnas
  means <- numeric(number_columns)  # inicializa una variable par alos promedios 
  for ( element in 1:number_columns){ # lee cada elemento
    means[i] <- mean(x[,element], na.rm = TRUE) # saca la media elininando los NA
  }
  means # regresa el valor
}

polutantmean <- function (directory, polutant, id = 1:332){
  polutant_values <- data.frame()
  ALL_FILES <- list.files(path = directory,full.names = TRUE)
  for (monitor in id){
    ##read_this_file <-read.csv(header = TRUE,file = monitor)
    polutant_values <- rbind(polutant_values,read.csv(header = TRUE,file = ALL_FILES[monitor]))
  }
  #get_polutant <- subset(polutant_values$polutant)
  #head(get_polutant)
  #means <- mean(polutant_values$polutant,na.rm = TRUE)
  MEAN <- mean(polutant_values[,polutant],na.rm = TRUE)
  #specific_pollutant <- polutant_values[polutant]
  #head(specific_pollutant)
  #class( polutant_values)
#  MEAN <- mean(specific_pollutant,na.rm = TRUE)
  MEAN
}

complete <- function (directory, id = 1:332){
  COMPLETE <- data.frame()
  #row.names(COMPLETE) <- c("ID","NOB")
  ALL_FILES <- list.files(path = directory,full.names = TRUE)
  for ( monitor in id ){
    #print(ALL_FILES[monitor])
    #COMPLETE <- rbind(COMPLETE,read.csv(header = TRUE,file = ALL_FILES[monitor]))
    CSV <- read.csv(header = TRUE,file = ALL_FILES[monitor])
    #head(CSV)
    df <- CSV[complete.cases(CSV),] # complete cases remoeve NA 
    complete_vector<-c(monitor,dim(df))
    #rint (complete_vector)
    COMPLETE = rbind(COMPLETE,complete_vector)
  }
  names (COMPLETE) <- c("ID","NOB","COLS")
  COMPLETE
}


corr <- function(directory,umbral = 0){
  ALL_FILES <- list.files(path = directory,full.names = TRUE)
  All_values <- data.frame()
  vec <-vector(mode="numeric", length=0)
  for (monitor in ALL_FILES){
    #print(monitor)
    CSV <- read.csv(header = TRUE,file = monitor)
    df <- CSV[complete.cases(CSV),] # complete cases remoeve NA
#    print(dim(df))
    HITS <- dim(df[1])
    #print(HITS[1])
    if (HITS > umbral){
      correlation = cor(CSV[2],CSV[3],use = "pairwise.complete.obs")
      vec <- c(vec,correlation)
      #print(correlation)
    } 
  }
  vec
}    