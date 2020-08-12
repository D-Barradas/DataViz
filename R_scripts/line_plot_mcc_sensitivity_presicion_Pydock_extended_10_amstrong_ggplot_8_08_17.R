setwd("Documentos/BM4_for_nip_analysis_again/")

library (ggplot2)
library(reshape2)
#p + geom_point(aes(colour = Type, shape= Type, size=2)) +geom_line(aes(color=Type,size =1)


my_data_zdock <- read.csv("tabla_presicion_and_sensitivity_nip_distancia_zdock.csv",header = T)
my_data_zdock.m <- melt(my_data_zdock, id =c("NIP_VALUE","DISTANCE_CUTOFF"))
only_10_ams_zdock_s <- my_data_zdock.m[which(my_data_zdock.m$variable == "SENSITIVITY_GLOBAL"),]
only_10_ams_zdock_p <- my_data_zdock.m[which(my_data_zdock.m$variable == "PRESICION_GLOBAL"),]
only_10_ams_zdock_m <- my_data_zdock.m[which(my_data_zdock.m$variable == "MCC_GLOBAL"),]
only_10_ams_zdock_z <- my_data_zdock.m[which(my_data_zdock.m$variable == "SPECIFICITY"),]
only_10_ams_global_all_zdock <- rbind( only_10_ams_zdock_s,only_10_ams_zdock_p,only_10_ams_zdock_m,only_10_ams_zdock_z)
q <- ggplot(only_10_ams_global_all_zdock,aes(NIP_VALUE,value))
q <- q + theme_bw()+
  geom_point(aes(colour= variable, shape = variable ))+
  geom_line(aes(color=variable)) +
  facet_grid( DISTANCE_CUTOFF ~ .)+
  scale_y_continuous(limits = c(0,1))+
  ggtitle("ZDock")+
  theme(plot.title = element_text(hjust = 0.5))

my_data_pydock <- read.csv("tabla_presicion_and_sensitivity_MCC_nip_distancia.csv", header = T)
my_data_pydock.m <- melt(my_data_pydock, id =c("NIP_VALUE","DISTANCE_CUTOFF"))
only_10_ams_pydock_s <- my_data_pydock.m[which(my_data_pydock.m$variable == "SENSITIVITY_GLOBAL"),]
only_10_ams_pydock_p <- my_data_pydock.m[which(my_data_pydock.m$variable == "PRESICION_GLOBAL"),]
only_10_ams_pydock_m <- my_data_pydock.m[which(my_data_pydock.m$variable == "MCC_GLOBAL"),]
only_10_ams_pydock_z <- my_data_pydock.m[which(my_data_pydock.m$variable == "SPECIFICITY"),]
only_10_ams_global_all_pydock <- rbind(only_10_ams_pydock_s,only_10_ams_pydock_p, only_10_ams_pydock_m,only_10_ams_pydock_z)
p<- ggplot(only_10_ams_global_all_pydock,aes(NIP_VALUE,value))
p <- p+ theme_bw()+
  geom_point(aes(colour= variable, shape = variable ))+
  geom_line(aes(color=variable)) +
  facet_grid( DISTANCE_CUTOFF ~ .)+
  scale_y_continuous(limits = c(0,1))+
  ggtitle("PyDock")+
  theme(plot.title = element_text(hjust = 0.5))

my_data_max <- read.csv("tabla_presicion_and_sensitivity_nip_distancia_MAX_strategy.csv", header = T)
my_data_max.m <- melt(my_data_max, id =c("NIP_VALUE","DISTANCE_CUTOFF"))
only_10_ams_max_s <- my_data_max.m[which(my_data_max.m$variable == "SENSITIVITY_GLOBAL"),]
only_10_ams_max_p <- my_data_max.m[which(my_data_max.m$variable == "PRESICION_GLOBAL"),]
only_10_ams_max_m <- my_data_max.m[which(my_data_max.m$variable == "MCC_GLOBAL"),]
only_10_ams_max_z <- my_data_max.m[which(my_data_max.m$variable == "SPECIFICITY"),]
only_10_ams_global_all_max <- rbind(only_10_ams_max_s,only_10_ams_max_p,only_10_ams_max_m,only_10_ams_max_z)
g <- ggplot(only_10_ams_global_all_max, aes(NIP_VALUE,value))
g <- g +theme_bw()+
  geom_point(aes(colour= variable, shape = variable ))+
  geom_line(aes(color=variable)) +
  facet_grid( DISTANCE_CUTOFF ~ .)+
  scale_y_continuous(limits = c(0,1))+
  ggtitle("NIP max")+
  theme(plot.title = element_text(hjust = 0.5))

my_data_zd_pd <- read.csv("tabla_presicion_and_sensitivity_nip_distancia_zdock_evaluado_con_pydock.csv",header = T)
my_data_zdpd.m <- melt(my_data_zd_pd,id =c("NIP_VALUE","DISTANCE_CUTOFF") )
only_10_ams_zdpd_s <- my_data_zdpd.m[which(my_data_zdpd.m$variable == "SENSITIVITY_GLOBAL"),]
only_10_ams_zdpd_p <- my_data_zdpd.m[which(my_data_zdpd.m$variable == "PRESICION_GLOBAL"),]
only_10_ams_zdpd_m <- my_data_zdpd.m[which(my_data_zdpd.m$variable == "MCC_GLOBAL"),]
only_10_ams_zdpd_z <- my_data_zdpd.m[which(my_data_zdpd.m$variable == "SPECIFICITY"),]
only_10_ams_global_all_zdpd <- rbind(only_10_ams_zdpd_s,only_10_ams_zdpd_p,only_10_ams_zdpd_m,only_10_ams_zdpd_z)
t <- ggplot(only_10_ams_global_all_zdpd, aes(NIP_VALUE,value))
t <- t + theme_bw()+
  geom_point(aes(colour= variable, shape = variable ))+
  geom_line(aes(color=variable)) +
  facet_grid( DISTANCE_CUTOFF ~ .)+
  scale_y_continuous(limits = c(0,1)) +
  ggtitle("ZDock eval. w/PyDock")+
  theme(plot.title = element_text(hjust = 0.5))