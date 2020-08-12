library("ggplot2", lib.loc="/home/dbarrada/R/x86_64-suse-linux-gnu-library/3.2")

library(reshape2)
setwd("Dropbox/Tesis_drafts/scoring_paper/final_versions_of_paper/")
#Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}


df <- read.csv("data_graficas_s1_paper_scoring.csv",header = T)
FTDOCK <- df[ which(df$Method == "FTDock"),] 
ZDOCK <- df[ which(df$Method == "ZDOCK"),]
SDOCK <- df[ which(df$Method == "SDOCK"),] 

F <- FTDOCK [ order(FTDOCK$Top10,FTDOCK$Top1),]
Z <- ZDOCK [ order(ZDOCK$Top10,ZDOCK$Top1),]
S <- SDOCK [ order(SDOCK$Top10,SDOCK$Top1),]

F$T10 <- (F[,4]-F[,3])
F$T100 <- (F[,5]-F[,4])
F$T1 <- F[,3]
new_FTDOCK <- F[c("Method","Scoring.function","T1","T10","T100")]
colnames(new_FTDOCK) <- c("Method","Scoring.function","Top1","Top10","Top100")

Z$T10 <- (Z[,4]-Z[,3])
Z$T100 <- (Z[,5]-Z[,4])
Z$T1 <- Z[,3]
new_ZDOCK <- Z[c("Method","Scoring.function","T1","T10","T100")]
colnames(new_ZDOCK) <- c("Method","Scoring.function","Top1","Top10","Top100")

S$T10 <- (S[,4]-S[,3])
S$T100 <- (S[,5]-S[,4])
S$T1 <- S[,3]
new_SDOCK <- S[c("Method","Scoring.function","T1","T10","T100")]
colnames(new_SDOCK) <- c("Method","Scoring.function","Top1","Top10","Top100")
fdt.m <- melt(new_FTDOCK,id=c("Method","Scoring.function"))
sdt.m <- melt(new_SDOCK,id=c("Method","Scoring.function"))
zdt.m <- melt(new_ZDOCK,id=c("Method","Scoring.function"))

p <-  ggplot(fdt.m,aes(x=Scoring.function, y=value, fill = variable))
q <- ggplot(zdt.m,aes(x=Scoring.function, y=value, fill = variable ))
r <-ggplot(sdt.m,aes(x=Scoring.function, y=value, fill = variable))

my_theme <-  theme_bw()+theme(  
  axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.5, size= 14)
                                ,legend.title=element_blank()
                                ,axis.text.y = element_text(size = 14)
                                )
  
  #heme(axis.text.x = element_text( size= 14))+ 

p <- p +geom_bar(stat='identity',colour="Grey")+my_theme+
   scale_x_discrete(limits = fdt.m$Scoring.function)+
  ylab("Success rate")+ ylim(0,55)+ xlab("")
p <- p+scale_fill_grey(start = .45, end = .9)
#+
  #geom_histogram(binwidth = 0.5)+ #scale_fill_grey(start = .45, end = .9)+ 
#  coord_flip()+
  
 # theme(legend.position="none")

q <- q +geom_bar(stat='identity',colour="Grey")+my_theme+
  #geom_histogram(binwidth = 0.5)+
  scale_x_discrete(limits = zdt.m$Scoring.function)+
  ylab("")+ ylim(0,55)+ 
  #scale_fill_grey(start = .45, end = .9)+ 
  #  coord_flip()+
  xlab("")
q <- q+scale_fill_grey(start = .45, end = .9)
 # theme(legend.position="none")

r <- r +geom_bar(stat='identity',colour="Grey")+my_theme+
  #geom_histogram(binwidth = 0.5)+
  scale_x_discrete(limits = sdt.m$Scoring.function)+
  ylab("")+  ylim(0,55)+ 
  #scale_fill_grey(start = .45, end = .9)+ 
  #  coord_flip()+
  xlab("")
  #theme(legend.position="bottom")
r<- r+scale_fill_grey(start = .45, end = .9)
multiplot(p,q,r, cols=3)