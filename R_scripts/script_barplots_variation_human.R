df <- read.delim ("/home/didier/Dropbox/interactomica/RESULTS_INTERACTOMA_CORE/Analisis_tipo_stembeg_interactoma_core_diseasome_structures_and_models_20_01_17.csv", header = T) 
library(RColorBrewer)  
library(reshape2)
library (ggplot2)
my_theme <-  theme_bw()+theme(  
  axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5, size= 14)
  ,legend.title=element_blank()
  ,axis.text.y = element_text(size = 14)
)
hm.palette <- colorRampPalette(rev(brewer.pal(11, 'Spectral')), space='Lab')
df.melt(df, id = c("Zone","Type"))
df_missense <- df[ which(df$Type=="Missense"),]
df_Gain <- df[ which(df$Type=="Gain"),]
p <- ggplot(df_missense,aes(Zone , SNPs,fill = Database))
p + facet_grid(Database ~ . )+ geom_bar(stat='identity',position="dodge")+ my_theme
s <- ggplot(df_Gain, aes(Zone , SNPs,fill = Database))
s + facet_grid(Database ~ . )+ geom_bar(stat='identity',position="dodge")+ my_theme