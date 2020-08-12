#setwd("Dropbox/interactomica/")
#install.packages("extrafont")### para instalar en las maquinas
#library(extrafont)
#font_import()  #### est instala y toma un tiempo
#loadfonts(device="win")       #Register fonts for Windows bitmap output
#fonts()                       #vector of font family names
#http://stackoverflow.com/questions/26218002/r-manually-set-shape-by-factor
# x <- read.csv("Analisis_tipo_stemberg_6_enfermedades_modelos_estructuras.csv")
# e <- read.csv("Analisis_tipo_stemberg_6_enfermedades_solo_estructuras.csv")
# f <- read.csv("Analisis_tipo_stemberg_6_enfermedades_solo_modelos.csv")
 x <- read.csv("Analisis_tipo_stemberg_interactoma_y_core_modelos_estructuras.csv")
 e <- read.csv("Analisis_tipo_stemberg_interactoma_y_core_solo_estructuras.csv")
 f <- read.csv("Analisis_tipo_stemberg_interactoma_y_core_solo_modelos.csv")
require(ggplot2)
library(scales)
# d=data.frame(a=c("Disease", "Polymorphims", "Unclassified"))
#myTicks<-c(0.0,1.0,2.0,3.0)
#scaleFUN <- function(x) sprintf("%.2f", x)

 forestplot <- function(d){
 require(ggplot2)
# p <- ggplot(d, aes(x=x, y=y, ymin=ylo, ymax=yhi, col=type,shape = type))+geom_pointrange() +coord_flip()+scale_x_discrete(limits = rev(levels(d$x)))
  p <- ggplot(d, aes(x=x, y=y, ymin=ylo, ymax=yhi, col=type, shape = type))+
#  p <- ggplot(d, aes(x=x, y=y, ymin=ylo, ymax=yhi, col=shapes, shape = shapes))+

  scale_shape_discrete(solid=T) +
 # geom_pointrange(size = 1) +
  geom_point(size = 7.5)+
  geom_errorbar( width=0.2)+
  geom_hline(aes(x=0),yintercept=0, lty=2) +
  coord_flip()+
  scale_x_discrete(limits = rev(levels(d$x)))
  #+scale_y_continuous(limits=c(0.0, 3.0),breaks=seq(0, 3.0, by = 0.3))
  #+scale_y_continuous(breaks = c(0,1,2,3), labels = c("0.0", "1.0", "2.0","3.0"))
  #+scale_y_continuous(limits = c(0, 3))
  
 return(p)
 }


shapex <- c(16,17,15)
names(shapex) <- c("Disease","Polymorphism","Unclassified")

gg_color_hue <- function(n) { # ggplot default colors
  hues = seq(15, 375, length=n+1)
  hcl(h=hues, l=65, c=100)[1:n]
}
colors <- gg_color_hue(5)
names(colors) <- names(shapex)

my_theme <-  theme( 
  axis.text.y = element_text(face="bold",color="black",size =24) 
  ,axis.text.x = element_text(face="bold",color="black",size =24)
  ,panel.grid.major = element_line(size = 0.5)
  ,legend.position="top"
  #,legend.direction="vertical"
  ,legend.direction="horizontal"
  ,legend.key.size = unit(1.330, "cm")
  ,legend.text = element_text(color="black",size =24)
  ,legend.title = element_text(color="black",size =24))
#,text=element_text(family="Arial"))
 #,text=element_text(family="Arial", face="bold", size=12))
  #  ,legend.text = element_text(face="bold",color="black",size =28)
 # ,legend.title = element_text(face="bold",color="black",size =28))
  
  #scale_y_discrete(limits = c(0.0,1.0,2.0))+
  
  

 forestplot(x) + ylab("Odds_ratio") + xlab("") +
  #ylim ( range(myTicks))+
 # ylim ( c(0.0,3.0))+
   # scale_y_continuous(limits = c(0, 3))
  #geom_point(size = 4) +
  scale_shape_manual(values=shapex) + 
  scale_color_manual(values=colors) + 
  my_theme + scale_y_continuous(limits = c(0,3), breaks = c(0,1,2,3),labels = c("0.0","1.0","2.0","3.0"))

  ggsave("odds_ratio_modelos_estructuras.png")
#  ggsave("odds_ratio_modelos_estructuras_interactome_03_11_16.png")

 forestplot(f) + ylab("Odds_ratio")+ xlab("") + 
 #ylim ( c(0.0,3.0))+
 # geom_point(size = 4) +
  scale_shape_manual(values=shapex) + 
  scale_color_manual(values=colors) + 
  my_theme + 
  scale_y_continuous(limits = c(0,3), breaks = c(0,1,2,3),labels = c("0.0","1.0","2.0","3.0"))

 ggsave("odds_ratio_solo_modelos.png")
# ggsave("odds_ratio_solo_modelos_interactome_03_12_16.png")

 forestplot(e)+ ylab("Odds_ratio")+ xlab("") + 
#  ylim ( c(0,3))+
 # geom_point(size = 4) +
  scale_shape_manual(values=shapex) + 
  scale_color_manual(values=colors) + 
  my_theme + 
  scale_y_continuous(limits = c(0,3), breaks = c(0,1,2,3),labels = c("0.0","1.0","2.0","3.0"))

 ggsave("odds_ratio_solo_estructuras.png")
#ggsave("odds_ratio_solo_estructuras_interactome_03_12_16.png")
#ggsave(file="test.svg", plot=test, width=10, height=8)#
# forestplot(x) + ylab("Odds_ratio") + xlab("") + theme(axis.text.y = element_text(face="bold",color="black",size =28)) +theme(axis.text.x = element_text(face="bold",color="black",size =28)) + theme(panel.grid.major = element_line(size = 4))+ geom_point(size = 8)+theme(legend.position = "top") + theme(legend.text = element_text(face="bold",color="black",size = 28))+ theme(legend.title = element_text(face="bold",color="black",size =28))+theme(legend.position = c(0.00,0.9))
# ggsave("odds_ratio_interactoma_core_modelos_estructuras.png")
# forestplot(f) + ylab("Odds_ratio")+ xlab("") + theme(axis.text.y = element_text(face="bold",color="black",size =28))+  theme(panel.grid.major = element_line(size = 4))+ geom_point(size = 8)+theme(legend.position = "top")+ theme(legend.text = element_text(face="bold",color="black",size = 28))+ theme(legend.title = element_text(face="bold",color="black",size =28))+theme(legend.position = c(0.00,0.9))+theme(axis.text.x = element_text(face="bold",color="black",size =28))
# ggsave("odds_ratio_interactoma_core_solo_modelos.png")
# forestplot(e)+ ylab("Odds_ratio")+ xlab("") + theme(axis.text.y = element_text(face="bold",color="black",size =28)) + theme(panel.grid.major = element_line(size = 4))+ geom_point(size = 8) + theme(legend.position = c(0.00,0.9))+ theme(legend.text = element_text(face="bold",color="black",size =28))+ theme(legend.title = element_text(face="bold",color="black",size =28)+theme(legend.justification=c(1,1)))+theme(axis.text.x = element_text(face="bold",color="black",size =28))
# ggsave("odds_ratio_interactoma_core_solo_estructuras.png")
##
for ( i in seq_along(x$type)){
  print (i)
  if( x$type[i] == "Disease"){
    #print ("25")
    #print (nrow(x))
    x$shapes[i] <- "circle"
  }
  if (x$type[i] == "Unclassified"){
    #print ("15")
    x$shapes[i] <- "square"
  }
}



