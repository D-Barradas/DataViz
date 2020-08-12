# coding: utf-8
from operator import itemgetter
combo = []
combo_fd,combo_zd,combo_sd = [],[],[]
top10_sf_fd = [x.strip() for x in open("top10_sf_for_bm4_ftdock.txt").readlines()]
top10_sf_zd = [x.strip() for x in open("top10_sf_for_bm4_zdock.txt").readlines()]
top10_sf_sd = [x.strip() for x in open("top10_sf_for_bm4_sdock.txt").readlines()]
top_combos_fd , top_combos_zd , top_combos_sd = [], [],[]
for x in top10_sf_fd:
    for y in top10_sf_fd:
        if x == y :
            break
        else:
            top_combos_fd.append((x,y))
            
print top_combos_fd
for x in top10_sf_zd:
    for y in top10_sf_zd:
        if x == y :
            break
        else:
            top_combos_zd.append((x,y))
            
for x in top10_sf_sd:
    for y in top10_sf_sd:
        if x == y :
            break
        else:
            top_combos_sd.append((x,y))
            
read_the_success_file  = open("success_rate_BM5_best_scoring_functions_all_combos_BM4_BM5.txt").readlines()
        
combinations = []
for x in top_combos_fd:
    for y in top_combos_zd:
        for z in top_combos_sd:
            combinations.append((x,y,z))
final_combo = []           
for line in read_the_success_file:
    for c in combinations:
        if c[0][0] in line and c[0][1] in line and c[1][0] in line and c[1][1] in line and c[2][0] in line and c[2][1] in line:
            if line not in final_combo:
                final_combo.append(line)

final_combo_2 = [x.split() for x in final_combo]
outfile = open('success_rate_topsf_in_bm4_eval_bm5.csv','w')
for x in sorted(final_combo_2, key=itemgetter(2,1)):
 #   name = x[0].split('_')
 #   print len(name)
 #   print name
#    new_name = '%s %s_%s and %s_%s %s %s_%s and %s_%s %s %s_%s and %s_%s'%(name[0],name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9],name[10],name[11],name[12],name[13],name[14])
    outfile.write('%s,%s,%s,%s\n'%(x[0],x[1],x[2],x[3]))
