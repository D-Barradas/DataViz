library("ggplot2")
df <- read.csv("/home/didier/Dropbox/interactomica/RESULTS_INTERACTOMA_CORE/table_human_interactome_and_core_10_11_16_PTMs_en_interface_05_01_17_v2.csv",header=T)
data.frame(table(df$Type))
data.frame(table(df$PTM))
df2 <- df[ which(df$Type=="Disease"),]
number_of_snps_per_PTM <- data.frame(table(df2$PTM))
number_of_snps_per_PTM$type <- "Disease"
only_the_poly <- df[ which(df$Type=="Polymorphism"),]
number_of_snps_per_PTM_poly <- data.frame(table(only_the_poly$PTM))
number_of_snps_per_PTM_poly$type <- "Polymorphism"
only_the_unclass <- df[ which(df$Type=="Unclassified"),]
number_of_snps_per_PTM_unclass <- data.frame(table(only_the_unclass$PTM))
number_of_snps_per_PTM_unclass$type <- "Unclassified"
df_final <- rbind(number_of_snps_per_PTM,number_of_snps_per_PTM_poly,number_of_snps_per_PTM_unclass)
my_theme <-  theme_bw()+theme(  
  axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5, size= 14)
  ,legend.title=element_blank()
  ,axis.text.y = element_text(size = 14)
)
p <- ggplot(df_final, aes(Var1, Freq, fill = type)) 
p <- p+geom_bar(stat='identity', position="dodge")+ scale_fill_hue(l=40)+ my_theme
df_final_2 <- rbind(number_of_snps_per_PTM,number_of_snps_per_PTM_poly)
q <- ggplot(df_final_2, aes(Var1, Freq, fill = type)) +geom_bar(stat='identity', position="dodge")+ scale_fill_hue(l=40)+ my_theme
q <- q + ylab("Number of SNPs")+ xlab("Post translational modification")
p <- p + ylab("Number of SNPs")+ xlab("Post translational modification")