import scipy.cluster.hierarchy as sch
import pylab
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
#SDOCK_LABELS=['CP_BFKV', 'CP_HLPL', 'CP_TB', 'CP_TSC', 'AP_MPS', 'SDOCK']
#SDOCK_LABELS=['CP_BFKV', 'CP_BL', 'CP_BT', 'CP_GKS', 'CP_HLPL', 'CP_MJPL', 'CP_MJ3h', 'CP_MJ2h', 'CP_MJ1', 'CP_MJ2', 'CP_MSBM', 'CP_MS', 'CP_Qa', 'CP_Qm', 'CP_Qp', 'CP_RO', 'CP_SKOb', 'CP_SKOa', 'CP_SJKG', 'CP_TD', 'CP_TEl', 'CP_TEs', 'CP_TS', 'CP_VD', 'CP_SKOIP', 'AP_DCOMPLEX', 'AP_dDFIRE', 'AP_DFIRE2', 'CP_RMFCEN1', 'CP_RMFCEN2', 'CP_RMFCA', 'CP_TB', 'CP_TSC', 'AP_T1', 'AP_T2', 'AP_DOPE', 'AP_DOPE_HR', 'AP_DARS', 'AP_URS', 'AP_MPS', 'AP_WENG', 'CP_DECK', 'CP_ZPAIR_CB', 'CP_ZLOCAL_CB', 'CP_ZS3DC_CB', 'CP_Z3DC_CB', 'CP_EPAIR_CB', 'CP_ELOCAL_CB', 'CP_ES3DC_CB', 'CP_E3DC_CB', 'CP_E3D_CB', 'CP_ZPAIR_MIN', 'CP_ZLOCAL_MIN', 'CP_ZS3DC_MIN', 'CP_Z3DC_MIN', 'CP_EPAIR_MIN', 'CP_ELOCAL_MIN', 'CP_ES3DC_MIN', 'CP_E3DC_MIN', 'CP_E3D_MIN', 'AP_calRW', 'AP_calRWp', 'AP_GOAP_ALL', 'AP_GOAP_DF', 'AP_GOAP_G', 'AP_PISA', 'SDOCK', 'ELE', 'DESOLV', 'VDW', 'PYDOCK_TOT', 'ODA', 'PROPNSTS', 'SIPPER']
#SDOCK_LABELS=['CP_BFKV', 'CP_HLPL', 'CP_Qp', 'CP_TB', 'CP_TSC', 'AP_T1', 'AP_T2', 'AP_MPS', 'AP_PISA', 'SDOCK'] ## all even overfitted
SDOCK_LABELS=['CP_BFKV', 'CP_RMFCEN1', 'CP_TB', 'AP_MPS', 'CP_E3D_MIN', 'AP_GOAP_DF', 'SDOCK', 'PYDOCK'] ## best combos
#ZDOCK_LABELS=['CP_TB', 'CP_TSC', 'AP_T1', 'AP_T2', 'AP_PISA', 'zdock3', 'CP_HLPL', 'ELE', 'PYDOCK_TOT', 'CP_BT'] ## all even overfitted
#ZDOCK_LABELS=['CP_TB', 'AP_T1', 'AP_T2', 'zdock3', 'CP_HLPL', 'ELE', 'PYDOCK_TOT', 'CP_BT']
ZDOCK_LABELS=['CP_TB', 'AP_T1', 'AP_T2', 'AP_PISA', 'zdock3', 'AP_calRWp', 'PYDOCK', 'CP_BFKV'] ## beast combos
#FTDOCK_LABELS=['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC'] ## all even overfitted
#FTDOCK_LABELS=['AP_dDFIRE', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_HLPL']
FTDOCK_LABELS=['AP_DCOMPLEX', 'AP_dDFIRE', 'CP_BFKV', 'PYDOCK', 'CP_SJKG', 'CP_SKOa'] ## best combos

if 'sdock' in sys.argv[1]:
	LABELS,mtd = SDOCK_LABELS,'sdock'
elif 'zdock' in sys.argv[1]:
	LABELS,mtd = ZDOCK_LABELS,'zdock'
elif 'ftdock' in sys.argv[1]:
	LABELS,mtd= FTDOCK_LABELS,'ftdock'
else:
	print "don't know whats this!"
#SDOCK_LABELS=['CP_BFKV', 'CP_BL', 'CP_BT', 'CP_GKS', 'CP_HLPL', 'CP_MJPL', 'CP_MJ3h', 'CP_MJ2h', 'CP_MJ1', 'CP_MJ2', 'CP_MSBM', 'CP_MS', 'CP_Qa', 'CP_Qm', 'CP_Qp', 'CP_RO', 'CP_SKOb', 'CP_SKOa', 'CP_SJKG', 'CP_TD', 'CP_TEl', 'CP_TEs', 'CP_TS', 'CP_VD', 'CP_SKOIP', 'AP_DCOMPLEX', 'AP_dDFIRE', 'AP_DFIRE2', 'CP_RMFCEN1', 'CP_RMFCEN2', 'CP_RMFCA', 'CP_TB', 'CP_TSC', 'AP_T1', 'AP_T2', 'AP_DOPE', 'AP_DOPE_HR', 'AP_DARS', 'AP_URS', 'AP_MPS', 'AP_WENG', 'CP_DECK', 'CP_ZPAIR_CB', 'CP_ZLOCAL_CB', 'CP_ZS3DC_CB', 'CP_Z3DC_CB', 'CP_EPAIR_CB', 'CP_ELOCAL_CB', 'CP_ES3DC_CB', 'CP_E3DC_CB', 'CP_E3D_CB', 'CP_ZPAIR_MIN', 'CP_ZLOCAL_MIN', 'CP_ZS3DC_MIN', 'CP_Z3DC_MIN', 'CP_EPAIR_MIN', 'CP_ELOCAL_MIN', 'CP_ES3DC_MIN', 'CP_E3DC_MIN', 'CP_E3D_MIN', 'AP_calRW', 'AP_calRWp', 'AP_GOAP_ALL', 'AP_GOAP_DF', 'AP_GOAP_G', 'AP_PISA', 'SDOCK', 'ELE', 'DESOLV', 'VDW', 'PYDOCK_TOT', 'ODA', 'PROPNSTS', 'SIPPER']
#= open(sys.argv[1]).readlines()
table_unison,table_simetric = np.loadtxt(sys.argv[1],delimiter=','),np.loadtxt(sys.argv[2],delimiter=',')
#data = np.loadtxt(sys.argv[1],delimiter=',')
#fig, ax = plt.subplots()
#heatmap = ax.pcolor(data)
#heatmap = plt.pcolor(data,cmap='RdBu')
#for y in range(data.shape[0]):
#    for x in range(data.shape[1]):
#	if data[y, x] < 23.00 :
#		mycolor= (1,1,1)
#	elif  data[y, x] > 34.70:
#		mycolor= (1,1,1) 
#	else :
#		mycolor = (0,0,0)
#       	#plt.text(x + 0.5, y + 0.5, '%.2f' % data[y, x],color=mycolor,fontsize=3,
#       	plt.text(x + 0.5, y + 0.5, '%.2f' % data[y, x],color=mycolor,fontsize=12,
#                 horizontalalignment='center',
#                 verticalalignment='center',
#                 )

#ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
#ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

#ax.set_xticklabels(LABELS,fontsize=13, rotation=-90,minor=False)
#ax.set_yticklabels(LABELS,fontsize=13, minor=False)
#cbar = plt.colorbar(heatmap)#fig.colorbar()
###plt.colorbar()
#plt.show()
for num,D in enumerate([table_unison,table_simetric]):
#for num,D in enumerate([table]):
#D = table_unison

	if num == 0:
		label= '_unison'
	if num ==1:
		label = '_simetric'	


	# Compute and plot first dendrogram.
	print 'computing dendogram'
	fig = pylab.figure()
	ax1 = fig.add_axes([0.02,0.1,0.14,0.6])### original
#	ax1 = fig.add_axes([0.3,0.82,0.6,0.06]) ### modified , de este hay que modificar  bottom ,height
	Y = sch.linkage(D, method='single')
#	Y = sch.linkage(D, method='centroid')
	#Z1 = sch.dendrogram(Y, orientation='right',labels=array(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC']))
	Z1 = sch.dendrogram(Y,orientation='right')#,labels=array(['CP_DECK', 'AP_dDFIRE', 'AP_PISA', 'CP_BFKV', 'CP_TB', 'pydock', 'CP_RMFCA', 'CP_HLPL', 'CP_TSC']))
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
#	ax2 = fig.add_axes([0.065,0.1,0.1,0.6]) ### de este hay que modificar letf , width
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
	label1=	LABELS
	#label1 = [table[m] for m in idx1 ]
#	label2 = [table[m] for m in idx2 ]
	axmatrix.set_xticks(range(len(D)))
	axmatrix.set_xticklabels(label1, minor=False)
	axmatrix.xaxis.set_label_position('top')
	axmatrix.set_yticks(range(len(D)))
	axmatrix.set_yticklabels(label1, minor=False)
#	axmatrix.set_yticklabels(label2, minor=False)
	axmatrix.yaxis.set_label_position('left')
	#axmatrix.yaxis.tick_right()
	
	#axmatrix.xaxis.tick_bottom()
	#
	pylab.xticks(rotation=-90,fontsize=11)
	pylab.yticks(fontsize=11)
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
	### PLot number on squares:
#	for y in range(D.shape[0]):
#	    for x in range(D.shape[1]):
#		if D[y, x]>17.00 :
#			color = (0.0, 0.0, 0.0) 
#		elif D[y, x] <30.00:
#            		color = (0.0, 0.0, 0.0)
#        	else:
#            		color = (1.0, 1.0, 1.0)
#        	plt.text(x + 0.13, y + 0.13, '%.2f' % D[y, x],color=color,fontsize=10,horizontalalignment='center',verticalalignment='center', )
##plt.show()
#
#	## Plot colorbar.
	axcolor = fig.add_axes([0.92,0.1,0.02,0.6])
#	pylab.colorbar(im, cax=axcolor)
	pylab.colorbar(im,cax=axcolor,format='%1i')
##	fig.show()
	fig.savefig('heatmap_best_combos_top10_%s_%s.png'%(label,mtd))

	
	
