setwd("../Tesis_drafts/scoring_paper/final_versions_of_paper/")
df <- read.csv("figura_4_data_success_rate.csv")
library("ggplot2", lib.loc="/home/dbarrada/R/x86_64-suse-linux-gnu-library/3.2")
  
library(reshape2)


FTDOCK <- df[ which(df$Method == "FTDock"),] 
ZDOCK <- df[ which(df$Method == "ZDOCK"),]
SDOCK <- df[ which(df$Method == "SDOCK"),] 

F <- FTDOCK [ order(-FTDOCK$Top10,-FTDOCK$Top1),]
Z <- ZDOCK [ order(-ZDOCK$Top10,-ZDOCK$Top1),]
S <- SDOCK [ order(-SDOCK$Top10,-SDOCK$Top1),]

F$T10 <- (F[,4]-F[,3])
F$T100 <- (F[,5]-F[,4])
F$T1 <- F[,3]
new_FTDOCK <- F[c("Method","Scoring.function","T1","T10","T100")]

Z$T10 <- (Z[,4]-Z[,3])
Z$T100 <- (Z[,5]-Z[,4])
Z$T1 <- Z[,3]
new_ZDOCK <- Z[c("Method","Scoring.function","T1","T10","T100")]

S$T10 <- (S[,4]-S[,3])
S$T100 <- (S[,5]-S[,4])
S$T1 <- S[,3]
new_SDOCK <- S[c("Method","Scoring.function","T1","T10","T100")]
#df1 <- melt(new_FTDOCK,id.vars = "Scoring.function")
#df1 <- melt(new_FTDOCK,id=c("Method","Scoring.function"))
fdt.m <- melt(new_FTDOCK,id=c("Method","Scoring.function"))
sdt.m <- melt(new_SDOCK,id=c("Method","Scoring.function"))
zdt.m <- melt(new_ZDOCK,id=c("Method","Scoring.function"))

p <-  ggplot(fdt.m,aes(x=Scoring.function, y=value*100, fill = variable))
q <- ggplot(zdt.m,aes(x=Scoring.function, y=value*100, fill = variable ))
r <-ggplot(sdt.m,aes(x=Scoring.function, y=value*100, fill = variable))


p +geom_bar(stat='identity',colour = "Grey")+
  
  #geom_histogram(binwidth = 0.5)+
  theme_bw()+
  #theme(axis.text.x = element_text(angle = 90, hjust = 1,size= 14))+ 
  #heme(axis.text.x = element_text( size= 14))+ 
  scale_x_discrete(limits = fdt.m$Scoring.function)+
  ylab("Percentage")+ ylim(0,60)+ 
  theme(legend.title=element_blank())+
  theme(axis.text.y = element_text(size = 14))+
  scale_fill_grey(start = .45, end = .9)+ 
  coord_flip()+
  xlab("")

q +geom_bar(stat='identity',colour = "Grey")+
  theme_bw()+
  #theme(axis.text.x = element_text(angle = 90, hjust = 1,size= 14))+ 
  theme(axis.text.x = element_text( size= 14))+ 
  scale_x_discrete(limits = zdt.m$Scoring.function)+
  ylab("Percentage")+ ylim(0,60)+
  theme(legend.title=element_blank())+
  theme(axis.text.y = element_text(size = 14))+
  scale_fill_grey(start = .45, end = .9)+ coord_flip()+
  xlab("")



r +geom_bar(stat='identity',colour = "Grey")+
  theme_bw()+
  #theme(axis.text.x = element_text(angle = 90, hjust = 1,size= 14))+ 
  theme(axis.text.x = element_text( size= 14))+ 
  scale_x_discrete(limits = sdt.m$Scoring.function)+
  ylab("Percentage")+ ylim(0,60)+
  theme(legend.title=element_blank())+
  theme(axis.text.y = element_text(size = 14))+
  scale_fill_grey(start = .45, end = .9)+ 
  coord_flip()+
  xlab("")