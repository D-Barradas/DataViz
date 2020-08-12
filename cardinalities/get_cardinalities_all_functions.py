### Usage python this_program.py pdb.list
###
def no_repeat(lista):
	unico = set()
	for m in lista:
		if m not in unico:
			unico.add(m)
	return unico

#from libpydock.util.Table import Table
#from numpy import array
import numpy as np
import os
import sys
import scipy
import pylab
import scipy.cluster.hierarchy as sch
#import scipy
#D = scipy.zeros([73,73])
#INPUT =[m.strip() for m in  open(sys.argv[1]).readlines()]
#print INPUT
DIR = os.listdir('.')

PDB_TO_READ = [x.strip() for x in open(sys.argv[1]).readlines()]
#table = [m [ for n in DIR if os.path.isdir(n)] for m in DIR if os.path.isdir(m) ]
#table = [m for m in DIR if os.path.isdir(m) if m in INPUT]
table = [m for m in DIR if os.path.isdir(m) ]
#table = [[m,n] for m in DIR if os.path.isdir(m) for n in DIR if os.path.isdir(n)]
print len(table)
print table
#table2 = [[(table[i],table[j])] for i in range(len(table)) for j in range(len(table))]
#table2 =[[]for i in range(len(table)) for j in range(len(table))]

#table_simetric= [[] for j,n in enumerate(table) ] for i,m in enumerate(table)  ]
#table_unison =  [[] for j,n in enumerate(table) ] for i,m in enumerate(table)  ]
table2= [[[] for j,n in enumerate(table) ] for i,m in enumerate(table)  ]
table_unison = scipy.zeros([len(table),len(table)])
table_simetric = scipy.zeros([len(table),len(table)])

#print table2
for i,m in enumerate(table):
	for j,n in enumerate(table):
		table2[i][j]=((m,n))
#		print i,j
#print table2
for i,m in enumerate(table2):
	for j,n in enumerate(m):	
	#	print n[0],n[1]
		PART_ONE, PART_TWO = set(),set()
		ONE = os.listdir(n[0])
		TWO = os.listdir(n[1])
	#	print ind,jnd
		for archive in ONE:
#			print n[0],archive
			
			if '.ene' in archive:
				BM_CASE = archive.split('.')[0].split('_')[-1]####CP_BFKV_3SGQ.ene
				ENE1= open('%s/%s'%(n[0], archive)).readlines()[2:12]
				if BM_CASE in PDB_TO_READ :
					for lines in ENE1:	
						CONFIG,CAPRI = lines.split()[0],lines.split()[-3]
						if CAPRI != 'incorr':
#						if BM_CASE not in PART_ONE :
							PART_ONE.add (BM_CASE)
#							break
	#			else :
	#				break
		for archive2 in TWO :
			if '.ene' in archive2:
				BM_CASE2 = archive2.split('.')[0].split('_')[-1]####CP_BFKV_3SGQ.ene
				ENE12= open('%s/%s'%(n[1], archive2)).readlines()[2:12]
#				print n[1],archive2
				if BM_CASE2 in PDB_TO_READ :
					for lines in ENE12:	
						CONFIG,CAPRI = lines.split()[0],lines.split()[-3]
						if CAPRI != 'incorr':
#							if BM_CASE2 not in PART_TWO :
							PART_TWO.add (BM_CASE2)
#							break
#				else:
#					break
	#		print archive2
		simetric_difference= no_repeat(PART_ONE) ^ no_repeat(PART_TWO)
		unison = no_repeat(PART_ONE) | no_repeat(PART_TWO)
#		simetric_difference= PART_ONE ^ PART_TWO
#		unison = PART_ONE & PART_TWO
#		table_simetric[i][j].append(len(simetric_difference))
#		table_unison[i][j].append(len(unison))
		table_simetric[i,j]= table_simetric[j,i]=len(simetric_difference)
		table_unison[i,j] = table_unison[j,i]=len(unison)
#print table_simetric
#print 
#print 
#print table_unison
np.savetxt('table_simetric_all_sf_bm5_ftdock.txt', table_simetric, delimiter=',')
#print table_simetric
#print 
#print 
np.savetxt('table_unison_all_sf_bm5_ftdock.txt', table_unison, delimiter=',')

for num,D in enumerate([table_unison,table_simetric]):
#D = table_unison

	if num == 0:
		label= '_unison'
	if num ==1:
		label = '_simetric'	


	# Compute and plot first dendrogram.
	print 'computing dendogram'
	fig = pylab.figure(figsize=(20,20))
	#ax1 = fig.add_axes([0.09,0.1,0.2,0.6])### original
	ax1 = fig.add_axes([0.3,0.8,0.6,0.15]) ### modified , de este hay que modificar  bottom ,height
	Y = sch.linkage(D, method='single')
#	Y = sch.linkage(D, method='centroid')
	#Z1 = sch.dendrogram(Y, orientation='right',labels=array(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC']))
	Z1 = sch.dendrogram(Y)#,labels=array(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC']))
	ax1.set_xticks([])
	ax1.set_yticks([])
	#ax1.set_xticks(range(len(table)))
	#ax1.set_yticks(range(len(table)))
	#ax1.set_xticklabels(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC'])
	#ax1.set_yticklabels(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC'])
	#
	### Compute and plot second dendrogram.
	#qx2 = fig.add_axes([0.3,0.71,0.6,0.2])
	#ax2 = fig.add_axes([0.09,0.05,0.2,0.3]) ##[left, bottom, width, height]
#	ax2 = fig.add_axes([0.065,0.1,0.14,0.6]) ### de este hay que modificar letf , width
#	Y = sch.linkage(D, method='single')
#	Z2 = sch.dendrogram(Y,orientation='right')#, labels=array(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC']))
	#Z2 = sch.dendrogram(Y, labels=array(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC']))
#	ax2.set_xticks([])
#	ax2.set_yticks([])
	#ax2.set_xticklabels(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC'])
	#ax2.set_yticklabels(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC'])
	#
	### Plot distance matrix.
	axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
	idx1 = Z1['leaves']
#	idx2 = Z2['leaves']
	D = D[idx1,:]
#	D = D[:,idx2]
	D = D[:,idx1]
	##im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu)
	im = axmatrix.matshow(D, aspect='auto', origin='lower')
	axmatrix.set_xticks([])
	axmatrix.set_yticks([])
	#
	##print idx1
	##print label1
	
	## Plot axes labels
	label1 = [table[m] for m in idx1 ]
#	label2 = [table[m] for m in idx2 ]
	axmatrix.set_xticks(range(len(table)))
	axmatrix.set_xticklabels(label1, minor=False)
	axmatrix.xaxis.set_label_position('top')
	axmatrix.set_yticks(range(len(table)))
	axmatrix.set_yticklabels(label1, minor=False)
#	axmatrix.set_yticklabels(label2, minor=False)
	axmatrix.yaxis.set_label_position('left')
	#axmatrix.yaxis.tick_right()
	
	#axmatrix.xaxis.tick_bottom()
	#
	pylab.xticks(rotation=-90,fontsize=10)
	pylab.yticks(fontsize=10)
	#
	#label2 = [table[m] for m in idx2 ]
	#
	#axmatrix.set_yticks(range(len(table)))
	#axmatrix.set_yticklabels(label2, minor=False)
	#axmatrix.yaxis.set_label_position('left')
	#axmatrix.yaxis.tick_right()
	#
	#axcolor = fig.add_axes([0.94,0.1,0.02,0.6])
	#
	#
	## Plot colorbar.
	axcolor = fig.add_axes([0.92,0.1,0.02,0.6])
	pylab.colorbar(im, cax=axcolor)
	##fig.show()
	fig.savefig('dendrogram_FTdock_all_bm5%s.png'%label)
