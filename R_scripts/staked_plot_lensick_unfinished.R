setwd("/home/dbarrada/Dropbox/Docking/success_rate_para_articulo")
library(ggplot2)
library(RColorBrewer)  
library(reshape2)
df <- read.csv("success_rate_benchmark_lensick.csv",header = T)
df$TOP10 <- (df[,3]-df[,2])*100
df$TOP100 <- (df[,4]-df[,3])*100
df$TOP1 <- df[,2]*100
newdf <- df[c("Scoring.function","TOP1","TOP10","TOP100")]
df1 <- melt(newdf,id.vars = "Scoring.function")
#hm.palette <- colorRampPalette(rev(brewer.pal(9, 'Greys')), space='Lab')

#cbPalette <- c("#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")
ggplot(df1, aes(x = Scoring.function, y = value, fill=variable) )+
#ggplot(df1, aes(x = Scoring.function, y = value,colour=variable) ) +
  geom_bar(stat='identity',colour="Grey") + 
  #geom_bar(stat='identity',colour = hm.palette(100))+
   theme_bw()+
  theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust=0.5, size = 14))+ 
  scale_x_discrete(limits = df1$Scoring.function)+
  ylab("Percentage") + theme(legend.title=element_blank())+
  theme(axis.text.y = element_text(size = 14))+
  scale_fill_grey(start = 0.45, end = .9)

