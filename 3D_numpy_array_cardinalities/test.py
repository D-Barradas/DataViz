from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

unison = np.load("numpy_table_3D_union_cardinalities.txt")
x,y,z = (unison>24).nonzero()
#outfile = open('4_columns.csv','w')
#outfile.write('coor_x,coor_y,coor_z,cases\n')
fig = plt.figure()
print x
print y 
print z
ax = fig.add_subplot(111, projection='3d')
#ax.plot_trisurf(x,y,z,cmap=cm.jet, linewidth=0.2) ## sirve
ax.bar(x, y, zs=z, zdir='y',color = ['r', 'g', 'b', 'y'] , alpha=0.8)
plt.show()
#ax = fig.gca(projection='3d')
#for i,x in enumerate(unison):
##	XX = unison[x]
#	for j,y in enumerate(x):
##		YY = unison[x][y]
#		for k,z in enumerate(y):
#			outfile.write('%i,%i,%i,%i\n'%(i,j,k,unison[i][j][k]))
##			ZZ = unison[x][y][z]
##
#ax.scatter(x,y,-z , zdir='z', c= 'red')
#:plt.savefig("demo.png")
