#TU = np.array(table_unison)
#np.save(outfile_2,np.array(table_simetric
#"","ftdock","zdock","sdock","coor_x","coor_y","coor_z","cases"
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib
import sys
import pylab
from operator import itemgetter
#table_unison,table_simetric = np.loadtxt(sys.argv[1],delimiter=','),np.loadtxt(sys.argv[2],delimiter=',')
#TU = np.load(sys.argv[1])
READ_TABLE = open(sys.argv[1]).readlines()[1:]
RT,XX,YY,ZZ,corr_x,corr_y,corr_z,label_ftdock,label_zdock,label_sdock = [],[],[],[],[],[],[],[],[],[]
for line in READ_TABLE:
 #	w,x,y,z,ftdock,zdock,sdock= line.split(',')[6],line.split(',')[4],line.split(',')[5],line.split(',')[7],line.split(',')[1],line.split(',')[2],line.split(',')[3]
	ftdock,zdock,sdock,x,y,z,w=line.split(',')[1],line.split(',')[2],line.split(',')[3],line.split(',')[4],line.split(',')[5],line.split(',')[6],line.split(',')[7].strip()
	RT.append((float(x),float(y),float(z),ftdock,zdock,sdock,float(w)))
corr_w =[]
for rt in sorted(RT,key=itemgetter(2,0,1,-1),reverse=False):
	print rt
	x,y,z,ftdock,zdock,sdock = rt[0], rt[1], rt[2], rt[3], rt[4], rt[5]
	corr_x.append(x)
	corr_y.append(y)
	corr_z.append(z)
	corr_w.append(rt[6])
	ZZ.append(sdock)
	XX.append(ftdock)
	YY.append(zdock)
	if ftdock not in label_ftdock:
		label_ftdock.append(ftdock)
	if zdock not in label_zdock:
		label_zdock.append(zdock)
	if sdock not in label_sdock:
		label_sdock.append(sdock)
	
#unison = TU
#x,y,z = (unison>22 ).nonzero()
#rint len(unison>23)
#outfile = open('4_columns.csv','w')
#outfile.write('coor_x,coor_y,coor_z,cases\n'),
fig = plt.figure()
#print x,len(x)
#print y ,len(y)
#print z,len(z)
#ZZ = []
ax = fig.add_subplot(111, projection='3d')
#for valeu  in zip(x,y,z):
#	ZZ.append( unison[valeu[0],valeu[1],valeu[2]])
#	ZZ.append(unison[i][j][k])
colors = ['c','r', 'g', 'b', 'y','k','w']
	#cs = [c] * len(x)
#print ZZ,len(ZZ)
#x,y = range(0,48),range(0,48) 
#print x,y,len(x),len(y)
#ax.bar(x, y, zs=ZZ, zdir='y',color = colors, alpha=0.9)
labels_x,labels_y,labels_z=label_ftdock,label_zdock,label_sdock 		
#print corr_x,corr_y, corr_z
LZ = []
for n in range(6):
	for label in labels_z :	
		LZ.append(label)
print LZ
#ilabels_x,labels_y,labels_z= np.array(table),np.array(table2),np.array(table3)			
#ax.plot_trisurf(x,y,ZZ,cmap=pylab.cm.YlGnBu, linewidth=0.2) ## sirve
#sc = ax.bar(corr_x,corr_w, zs=corr_z, zdir='y',color = ['c','r', 'g', 'b', 'y'] , alpha=0.8)
#sc = ax.scatter(corr_x,corr_y, zs=corr_z,s=30,c=corr_w,color=colors) ### este es el bueno
#sc = ax.scatter(corr_x,corr_y, zs=corr_z,s=30,c=corr_w,cmap=plt.cm.prism) ### este es el bueno
sc = ax.scatter(corr_x,corr_y, zs=corr_z,s=30,c=corr_w,cmap=plt.cm.coolwarm) ### este es el bueno
#ax.scatter(corr_x,corr_y, zs=corr_z,s=20,c=corr_z,cmap=colors)
#ax.scatter(x, y, zs=ZZ, zdir='y', s=20, c=colors)

#ax.plot_surface(x,y,ZZ)
#X, Y,Z = np.meshgrid(x,y, ZZ)
#print X, Y
#ax.plot_surface(X, Y, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
#ax.set_xticks(range(len(labels_x)))
#ax.set_yticks(range(len(labels_y)))
ax.set_xticks(range(5))
ax.set_yticks(range(5))
ax.set_zticks(range(5))
ax.set_xticklabels(labels_x,size=5,color='g',rotation=-90,weight='bold')
ax.set_yticklabels(labels_y,size=5,color='r',rotation=-90,weight='bold')
ax.set_zticklabels(labels_z,size=5,color='b',weight='bold')
#ax.zticks(rotation=-90)
###ax.set_zticklabels(labels_z,size=5,color='b')
#ax.set_xlim3d(0,5)
#ax.set_xlim3d(0,5)
#ax.set_ylim3d(0,5)
#ax.set_zlim3d(21,25)
#ax.set_ylim3d(0,5)
ax.set_xlabel('Ftdock',size=5)
ax.set_ylabel('Zdock',size=5)
ax.set_zlabel('Sdock',size=5)

plt.colorbar(sc,format='%1i')

plt.show()
fig.savefig('demo.png')

#np.save('table_simetric_top10_ftdock.txt', table_simetric), delimiter=',')
