require (ggplot2)
#T <- read.csv("tabla_flex_only_w_solution_for_R_PYDOCK_TOT_FTDOCK.2.csv")
T <- read.csv("tabla_flex_for_R.2.csv")
x = NULL
y= NULL
z = NULL
contador <- 0
for (m in T$ENERGY_TOP1){ contador = contador +1
if(m != 0){ y <- append(y,T$ENERGY_TOP1[contador])
x<- append(x,T$dG[contador])
 z <- append (z ,as.character(T$TYPE[contador]))
}}
TOP1 <- data.frame(x,y,z)
qplot(TOP1$x,TOP1$y,shape=TOP1$z, color=TOP1$z,main="Docking ENERGY_TOP1 vs dG PYDOCK_TOT_FTDOCK",xlab = "dG",ylab="Docking energy")+ theme(axis.title=element_text(face="bold.italic",size="12", color="brown"), legend.position="top")+geom_smooth(method=lm,se=FALSE)

ggsave(file="All_bound_dG_ENERGY_TOP1_PYDOCK_TOT_FTDOCK.png")


#T <- read.csv("tabla_flex_only_w_solution_for_R_PYDOCK_TOT_FTDOCK.2.csv")
T <- read.csv("tabla_flex_for_R.2.csv")
x = NULL
y= NULL
z = NULL
contador <- 0
for (m in T$ENERGY_TOP10){ contador = contador +1
if(m != 0){ y <- append(y,T$ENERGY_TOP10[contador])
x<- append(x,T$dG[contador])
 z <- append (z ,as.character(T$TYPE[contador]))
}}
TOP10 <- data.frame(x,y,z)
qplot(TOP10$x,TOP10$y,shape=TOP10$z, color=TOP10$z,main="Docking ENERGY_TOP10 vs dG PYDOCK_TOT_FTDOCK",xlab = "dG",ylab="Docking energy")+ theme(axis.title=element_text(face="bold.italic",size="12", color="brown"), legend.position="top")+geom_smooth(method=lm,se=FALSE)

ggsave(file="All_bound_dG_ENERGY_TOP10_PYDOCK_TOT_FTDOCK.png")


#T <- read.csv("tabla_flex_only_w_solution_for_R_PYDOCK_TOT_FTDOCK.2.csv")
T <- read.csv("tabla_flex_for_R.2.csv")
x = NULL
y= NULL
z = NULL
contador <- 0
for (m in T$ENERGY_TOP100){ contador = contador +1
if(m != 0){ y <- append(y,T$ENERGY_TOP100[contador])
x<- append(x,T$dG[contador])
 z <- append (z ,as.character(T$TYPE[contador]))
}}
TOP100 <- data.frame(x,y,z)
qplot(TOP100$x,TOP100$y,shape=TOP100$z, color=TOP100$z,main="Docking ENERGY_TOP100 vs dG PYDOCK_TOT_FTDOCK",xlab = "dG",ylab="Docking energy")+ theme(axis.title=element_text(face="bold.italic",size="12", color="brown"), legend.position="top")+geom_smooth(method=lm,se=FALSE)

ggsave(file="All_bound_dG_ENERGY_TOP100_PYDOCK_TOT_FTDOCK.png")


#T <- read.csv("tabla_flex_only_w_solution_for_R_PYDOCK_TOT_FTDOCK.2.csv")
T <- read.csv("tabla_flex_for_R.2.csv")
x = NULL
y= NULL
z = NULL
contador <- 0
for (m in T$ENERGY_10K){ contador = contador +1
if(m != 0){ y <- append(y,T$ ENERGY_10K[contador])
x<- append(x,T$dG[contador])
 z <- append (z ,as.character(T$TYPE[contador]))
}}
T10K <- data.frame(x,y,z)
qplot(T10K$x,T10K$y,shape=T10K$z, color=T10K$z,main="Docking  ENERGY_10K vs dG PYDOCK_TOT_FTDOCK",xlab = "dG",ylab="Docking energy")+ theme(axis.title=element_text(face="bold.italic",size="12", color="brown"), legend.position="top")+geom_smooth(method=lm,se=FALSE)

ggsave(file="All_bound_dG_ENERGY_10K_PYDOCK_TOT_FTDOCK.png")

