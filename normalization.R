setwd('.')
library(stats)
files <- list.files(pattern = ".out4")
library(dplyr)
for (x in files){
  data <- read.delim (x, sep=" ", header = F)
  #dat <-read.delim(x,sep=",",header=F)
  #write.csv(data %>% mutate_each_(funs(scale),vars=c("V11","V18","V31")),x,col.names=F,row.names=FALSE,quote=F)
  #write.csv(dat %>% mutate_each_(funs(scale),vars=c("V11")),x,col.names=F,row.names=FALSE,quote=F)
  write.table(data %>% mutate_each_(funs(scale),vars=c("V11","V18","V31")),x,col.names=F,row.names=FALSE,quote=F)# TM-score_Global, Energy(total) ,TM_ave
                }
