# coding: utf-8
import sys
import os
combos_ftdock = [x.strip() for x in open("combos_ftdock.txt").readlines()]
combos_zdock = [x.strip() for x in open("combos_zdock.txt").readlines()]
combos_sdock = [x.strip() for x in open("combos_sdock.txt").readlines()]
read_results = [x.strip() for x in open("success_rate_BM5_best_scoring_functions_all_combos_BM4_BM5.txt").readlines()]
all_combos = []
for x in combos_ftdock:
    for y in combos_zdock:
        for z in combos_sdock:
            all_combos.append((x[6:],y[6:],z[6:]))
            
all_combos[1]
read_results[0]
read_results[10]
read_results[10].split('D_')
for m in read_results:
    FTD,ZD,SD = m.split('D_')[1],split('D_')[2],split('D_')[3]
    for n in all_combos:
        ftd,zd,sd = n[0],n[1],n[2]
        
all_results= []
for n in all_combos:
    ftd,zd,sd = n[0],n[1],n[2]
    for m in read_results:
        FTD,ZD,SD = m.split('D_')[1],m.split('D_')[2],m.split('D_')[3]
        if ftd in FTD and zd in ZD and sd in SD:
            if m not in all_results:
                all_results.append(m)
                
read_results = [x.strip() for x in open("success_rate_BM5_best_scoring_functions_all_combos_BM4_BM5.txt").readlines()[5:]]
get_ipython().magic(u'save get_the_results.py 1-17')
for n in all_combos:
    ftd,zd,sd = n[0],n[1],n[2]
    for m in read_results:
        FTD,ZD,SD = m.split('D_')[1],m.split('D_')[2],m.split('D_')[3]
        if ftd in FTD and zd in ZD and sd in SD:
            if m not in all_results:
                all_results.append(m)
                
all_results[0]
len(all_results)
outfile= open('results_filtered.txt','w')
for m in all_results:
    outfile.write(m)
    
for m in all_results:
    outfile.write(m+'\n')
    
get_ipython().magic(u'save get_the_results.py 1-24')
