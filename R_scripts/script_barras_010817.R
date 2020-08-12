library(RColorBrewer)  
library(reshape2)
library (ggplot2)
setwd("~/Documentos/")
my_theme <-  theme_bw()+theme(  
  axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5, size= 14)
  ,legend.title=element_blank()
  ,axis.text.y = element_text(size = 14)
)
### MCC va de -1 a 1 entonces no puedo poner porcentaje
my_data <- read.csv("resultados_mcc_interactoma_completo_31_07_17.csv")
hm.palette <- colorRampPalette(rev(brewer.pal(11, 'Spectral')), space='Lab')
pp<- ggplot(my_data,aes(Type,Value/100,fill= Mesurement))  
pp+ geom_bar(stat='identity',position="dodge",colour = "Grey")+ 
theme_bw() + 
scale_fill_grey()+
ylim(0,1)+
#scale_x_discrete(limits=c("Interface","SNPs","Disease","Polymorphism","Unclassified"))+
scale_x_discrete(limits=c("Unclassified","Polymorphism","Disease","SNPs","Interface"))+  
coord_flip()+
ylab("Value")+
xlab("")