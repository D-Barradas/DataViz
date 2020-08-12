import os

def read_my_csv (inputfile):
	names = []
	columna_top10 =[]
	FILE = open(inputfile).readlines()
	for n,linea in enumerate(FILE):
		values =linea.split(',')
		cols,nms =  values[1:6], values[0]	
		columna_top10.append(cols)
		names.append(nms) 
	return columna_top10,names		
	


for m in os.listdir('.'):
	if 'Success_rate_flex_BM4_BM5.csv' in m :
		CSV,LABEL = read_my_csv(m)
		print CSV
