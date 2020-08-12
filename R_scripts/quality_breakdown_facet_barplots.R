#df <- read.csv("~/Dropbox/CONSRANK_PROJECT/quality_breakdown_all_methods_consrank.csv")
df <- read.csv("~/Dropbox/CONSRANK_PROJECT/quality_breakdown_3K.csv")
df <- df[1:28,1:6]
#df <- df[,order("Method")]
print(head(df))
library(RColorBrewer)  
library(reshape2)
library (ggplot2)
#print (which( df$T100 > 100  ))
#setwd("~/Documentos/")
#setwd("~/Documentos/")
my_theme <-  theme_bw()+theme(  
  axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5, size= 14)
  ,legend.title=element_blank()
  ,axis.text.y = element_text(size = 14)
)
hm.palette <- colorRampPalette(rev(brewer.pal(11, 'Spectral')), space='Lab')
df.melt <- melt(df, id = c("Method","Cases","Class")) 
print(head(df.melt))
p <- ggplot(df.melt,aes( variable,value ,fill = Class))
p + facet_grid(Method ~ Cases ) + geom_bar(stat='identity',position="dodge")+ my_theme 
#p + facet_grid(Method ~ Cases ) + geom_bar(stat='identity',position="dodge")+ my_theme + ylim(0,100)