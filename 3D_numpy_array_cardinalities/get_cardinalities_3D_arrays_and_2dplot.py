def no_repeat(lista):
	unico = set()
	for m in lista:
		if m not in unico:
			unico.add(m)
	return unico

from numpy import array
import matplotlib.pyplot as plt
import os
import sys
import scipy
import pylab
import scipy.cluster.hierarchy as sch
import numpy as np

INPUT =[m.strip() for m in  open(sys.argv[1]).readlines()]
INPUT2 =[m.strip() for m in  open(sys.argv[2]).readlines()]
INPUT3 =[m.strip() for m in  open(sys.argv[3]).readlines()]
print INPUT
DIR = os.listdir('.')
BM5 = [x.strip() for x in  open(sys.argv[4]).readlines()]
table = [m for m in DIR if os.path.isdir(m) if m in INPUT]
table2 = [m for m in DIR if os.path.isdir(m) if m in INPUT2]
table3 = [m for m in DIR if os.path.isdir(m) if m in INPUT3]

#table2= [[[] for j,n in enumerate(table) ] for i,m in enumerate(table)  ] ##original line
table4= [[[[]for k,l in enumerate(table)] for j,n in enumerate(table) ] for i,m in enumerate(table)  ]

#table_unison = scipy.zeros((len(table),len(table),len(table)))
#table_simetric = scipy.zeros((len(table),len(table),len(table)))
#table_unison = np.zeros((len(table),len(table),len(table)))
#table_simetric = np.zeros((len(table),len(table),len(table)))
table_unison = [[[[]for k,l in enumerate(table)] for j,n in enumerate(table) ] for i,m in enumerate(table)  ]
table_simetric = [[[[]for k,l in enumerate(table)] for j,n in enumerate(table) ] for i,m in enumerate(table)  ]

#print table_unison
for i,m in enumerate(table):
	for j,n in enumerate(table2):
		for k,l in enumerate(table3):
			table4[i][j][k]=(m,n,l)
#print 'func1,func2,func3'

for i,m in enumerate(table4):
	for j,n in enumerate(m):	
		for k,l in enumerate(n):
			#print '%s,%s,%s'%(l[0],l[1],l[2])
			PART_ONE, PART_TWO , PART_THREE= set(),set(),set()
			ONE = os.listdir(l[0])
			TWO = os.listdir(l[1])
			THREE = os.listdir(l[2])
		#	print ind,jnd
			for archive in ONE:
	#			print n[0],archive
				if '.ene' in archive and '.zscore' in archive:
					BM_CASE = archive.split('.')[0]#### CP57.ene.zscore
					if BM_CASE in BM5:
						ENE1= open('%s/%s'%(l[0], archive)).readlines()[2:12]
						for lines in ENE1:	
							CONFIG,CAPRI = lines.split()[0],lines.split()[-3]
							if CAPRI != 'incorr':
							#	print BM_CASE
	#						if BM_CASE not in PART_ONE:
								PART_ONE.add(BM_CASE)
								#break
			for archive2 in TWO :
				if '.ene' in archive2 and 'zscore' in archive2:
					BM_CASE2 = archive2.split('.')[0]####CP_BFKV_3SGQ.ene
					if BM_CASE2 in BM5:
						ENE12= open('%s/%s'%(l[1], archive2)).readlines()[2:12]
	#					print n[1],archive2
						for lines in ENE12:	
							CONFIG,CAPRI = lines.split()[0],lines.split()[-3]
							if CAPRI != 'incorr':
	#						print BM_CASE2
		#					if BM_CASE2 not in PART_ONE:
								PART_TWO.add(BM_CASE2)
								#break
			for archive3 in THREE :
				if '.ene' in archive3 and 'zscore' in archive3:
					BM_CASE3 = archive3.split('.')[0]####CP_BFKV_3SGQ.ene
					if BM_CASE3 in BM5:
						ENE13= open('%s/%s'%(l[2], archive2)).readlines()[2:12]
	#					print n[1],archive2
						for lines in ENE13:	
							CONFIG,CAPRI = lines.split()[0],lines.split()[-3]
							if CAPRI != 'incorr':
	#						print BM_CASE2
		#					if BM_CASE2 not in PART_ONE:
								PART_THREE.add(BM_CASE3)
								#break
		#		print archive2
	#		print ',PART_ONE',no_repeat(PART_ONE)
	#		print ',PART_TWO',no_repeat(PART_TWO)
			simetric_difference= no_repeat(PART_ONE) ^ no_repeat(PART_TWO) ^ no_repeat(PART_THREE)
			unison = no_repeat(PART_ONE) | no_repeat(PART_TWO) | no_repeat(PART_THREE)
	#		table_simetric[i][j].append(len(simetric_difference))
	#		table_unison[i][j].append(len(unison))
	#		table_simetric[i,j]= table_simetric[j,i]=100* (float(len(simetric_difference))/231.)
	#		table_unison[i,j] =table_unison[j,i] = 100* (float(len(unison))/231.)
#			table_simetric[i,j,k]= table_simetric[k,j,i]=float(len(simetric_difference)) ## ORIGINAL
#			table_unison[i,j,k] =table_unison[k,j,i] = float(len(unison)) ## originl)
			table_simetric[i][j][k]= table_simetric[k][j][i]=len(simetric_difference)
			table_unison[i][j][k] =table_unison[k][j][i] = len(unison)
#print table_simetric	
#or m in table_simetric :
#for n in m :
#	print n



#outfile_2= open("numpy_table_3D_simetric_cardinalities.txt","w")
#outfile_1= open("numpy_table_3D_union_cardinalities.txt","w")
###outfile_1.write(table_unison)
###outfile_2.write(table_simetric)
#np.save( outfile_1,np.array(table_unison))
#np.save(outfile_2,np.array(table_simetric))



##TU = np.array(table_unison)
###np.save(outfile_2,np.array(table_simetric
##
##import matplotlib.pyplot as plt
##from mpl_toolkits.mplot3d import Axes3D
##from matplotlib import cm
##unison = TU
##x,y,z = (unison>20 ).nonzero()
###rint len(unison>23)
###outfile = open('4_columns.csv','w')
###outfile.write('coor_x,coor_y,coor_z,cases\n')
##fig = plt.figure()
##print x,len(x)
##print y ,len(y)
##print z,len(z)
##ZZ = []
##for valeu in zip(x,y,z):
##	ZZ.append( unison[valeu[0],valeu[1],valeu[2]])
##labels_x,labels_y,labels_z= np.array(table),np.array(table2),np.array(table3)			
##ax = fig.add_subplot(111, projection='3d')
##ax.plot_trisurf(x,y,z,cmap=cm.jet, linewidth=0.2) ## sirve
###x.bar(x, y, zs=z, zdir='y',color = ['r', 'g', 'b', 'y'] , alpha=0.8)
###x.scatter(x, y, zs=ZZ, zdir='y', s=20, c='r')
###ax.plot_surface(x,y,ZZ)
###X, Y = np.meshgrid(x, y)
###ax.plot_surface(X, Y, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
##ax.set_xticks([])
#ax.set_yticks([])
#ax.set_zticks([])
#ax.set_xticks(range(len(table)))
#ax.set_yticks(range(len(table)))
#ax.set_zticks(range(len(table)))
#ax.set_xticklabels(labels_x,minor= False,size=5,color='g')
#ax.set_yticklabels(labels_y,minor = False,size=5,color='y')
#ax.set_zticklabels(labels_z,minor = False,size=5,color='b')
#
#plt.show()

#np.save('table_simetric_top10_ftdock.txt', table_simetric), delimiter=',')
#print 
#print 
#np.savetxt('table_unison_top10_ftdock.txt', table_unison, delimiter=',')
#print table_unison
for num,D in enumerate([table_unison,table_simetric]):
#for num,D in enumerate([table_unison]):
#D = table_unison
	ZZ = []
	unison = np.array(D)
	x,y,z = (unison>20 ).nonzero()
	if num == 0:
		label= '_unison'
	if num ==1:
		label = '_simetric'	
	
	fig, ax1 = plt.subplots()
	for valeu in zip(x,y,z):
		ZZ.append( unison[valeu[0],valeu[1],valeu[2]])
	labels_x,labels_y,labels_z= np.array(table),np.array(table2),np.array(table3)			
	ax2 = ax1.twinx()
	ax1.plot(x, y, 'g-')
	ax2.plot(x, ZZ, 'b-')

	ax1.set_xlabel('x data')
	ax1.set_ylabel('y data', color='g')
	ax2.set_ylabel('z data', color='b')
#	plt.show()	
	## Plot colorbar.
#	axcolor = fig.add_axes([0.92,0.1,0.02,0.6])
#	pylab.colorbar(im, cax=axcolor)
	##fig.show()
	ax1.set_xticklabels(labels_x,minor= False,size=5,color='g')
	ax1.set_yticklabels(labels_y,minor = False,size=5,color='y')
	ax2.set_yticklabels(labels_z,minor = False,size=5,color='b')
	fig.savefig('dendrogram_success_rate_top_3mtd%s.png'%label)
	
	
