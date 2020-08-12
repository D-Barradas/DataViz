#library("ggplot2", lib.loc="/home/dbarrada/R/x86_64-suse-linux-gnu-library/3.2")
library("ggplot2")
library(reshape2)
setwd("/home/dbarrada/Dropbox/interactomica/RESULTS_INTERACTOMA_CORE")
df <- read.csv("datos_numero_de_nsSNPs_encontrados.csv")
my_theme <-  theme_bw()+theme(  
  axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5, size= 14)
  ,legend.title=element_blank()
  ,axis.text.y = element_text(size = 14)
)
df1 <- melt(df,id=c("Type","Zone"))



## haacer facetas por zona
p <- ggplot ( df1 , aes(x=Type ,y=value, fill= variable))+
  facet_grid(variable ~ Zone)+
  geom_bar(stat='identity', position="dodge")+
  my_theme+
  #scale_fill_hue(c=45, l=80) #### colores transparentes
  scale_fill_hue(l=40)
#ylab("# nsSNPs")
 # scale_x_discrete(limits = df1$Zone)
p+ ylab("# nsSNPs")