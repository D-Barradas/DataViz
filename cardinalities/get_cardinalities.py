#!/usr/bin/env python

import sys
import os
from libpydock.util.Table import Table

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(sel)
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

GLOBAL = os.listdir('.')
for line in GLOBAL:
        if os.path.isdir(line) and line != 'PYDOCK_TOT' or line != 'PYDOCK':
#       if os.path.isdir(line) and  line == 'HIGM_analysis' or line == 'LHON_analysis'  or line == 'VIH_suceptible':
#               print line
                with cd(line):
			DIR = os.listdir('.')
			FILES = []
			for f in DIR:
    				if '.ene' in f:
					FILES.append(f)

#def usage():
#    print "Usage: %s capri_score_file" % sys.argv[0]


#if __name__ == "__main__":
#    if len(sys.argv[1:]) != 1:
#        usage()
print "Complex,Top1_Acceptable;Top10_Acceptable;Top100_Acceptable;Top1000_Acceptable;Top1000_Acceptable;Top1_Medium;Top10_Medium;Top100_Medium;Top1000_Medium;Top10000_Medium;Top1_High;Top10_High;Top100_High;Top1000_High;Top10000_High"+ os.linesep
#        raise SystemExit("Wrong command line")

for files in sorted(FILES):
    capri_file= files.strip()
#   capri_file = sys.argv[1]
    complex_name = files.split('.')[0].split('_')[-1]
    data = Table.read(capri_file)
    
    top_1_acc = 0
    top_1_med = 0
    top_1_high = 0

    top_5_acc = 0
    top_5_med = 0
    top_5_high = 0

    top_10_acc = 0
    top_10_med = 0
    top_10_high = 0

    top_50_acc = 0
    top_50_med = 0
    top_50_high = 0

    top_100_acc = 0
    top_100_med = 0
    top_100_high = 0

    top_500_acc = 0
    top_500_med = 0
    top_500_high = 0

    top_1000_acc = 0
    top_1000_med = 0
    top_1000_high = 0

    top_5000_acc = 0
    top_5000_med = 0
    top_5000_high = 0

    top_10000_acc = 0
    top_10000_med = 0
    top_10000_high = 0
    
    print complex_name,
    #print "Complex;Top1_Acceptable;Top5_Acceptable;Top10_Acceptable;Top50_Acceptable;Top100_Acceptable;Top1_Medium;Top5_Medium;Top10_Medium;Top50_Medium;Top100_Medium;Top1_High;Top5_High;Top10_High;Top50_High;Top100_High" + os.linesep
    for i, score in enumerate(data['CAPRI']):
#print i,score
#       if score == '*':
	if 'acepta' in score:
            if i == 0:
                top_1_acc += 1
            if i < 5:
                top_5_acc += 1
            if i < 10:
                top_10_acc += 1
            if i < 50:
                top_50_acc += 1
	    
            if i < 100:
                top_100_acc += 1
	    if i < 1000:
		top_1000_acc += 1
            top_10000_acc += 1

 #           top_100_acc += 1
	    


#        if score == '**':
	if 'Med' in score:
            if i == 0:
                top_1_med += 1
            if i < 5:
                top_5_med += 1
            if i < 10:
                top_10_med += 1
            if i < 50:
                top_50_med += 1
 #           top_100_med += 1
            if i < 100:
                top_100_med += 1
            if i < 1000:
                top_1000_med += 1

            top_10000_acc += 1

#       if score == '***':
	if 'High' in score:
            if i == 0:
                top_1_high += 1
            if i < 5:
                top_5_high += 1
            if i < 10:
                top_10_high += 1
            if i < 50:
                top_50_high += 1
#            top_100_high += 1
            if i < 100:
                top_100_high+= 1
            if i < 1000:
                top_1000_high+= 1

            top_10000_high+= 1

#    print ';'.join([str(top_1_acc), str(top_5_acc), str(top_10_acc), str(top_50_acc), str(top_100_acc),
#                    str(top_1_med), str(top_5_med), str(top_10_med), str(top_50_med), str(top_100_med),
 #                   str(top_1_high), str(top_5_high), str(top_10_high), str(top_50_high), str(top_100_high),])
    print ';'.join([str(top_1_acc),  str(top_10_acc),  str(top_100_acc),str(top_1000_acc),str(top_10000_acc),
                    str(top_1_med),  str(top_10_med),  str(top_100_med),str(top_1000_med),str(top_10000_med),
                    str(top_1_high), str(top_10_high),  str(top_100_high),str(top_1000_high),str(top_10000_high),])
        
