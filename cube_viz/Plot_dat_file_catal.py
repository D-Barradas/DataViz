#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
from optparse import OptionParser


##Parse the options
usage = "USAGE: python Plot_dat_file_catal.py --f1 First_dat_file --f2 Second_dat_file --c1 Chem1 --c2 Chem2 --jobid PNG_file_name\n"
parser = OptionParser(usage=usage)

##options
parser.add_option("--f1",help="First data file", dest="f1")
parser.add_option("--f2",help="Second data file", dest="f2")
parser.add_option("--c1",help="Chemical for label 1", dest="c1")
parser.add_option("--c2",help="Chemical for label 2", dest="c2")

parser.add_option("--jobid",help="Job name for exit file", dest="jobid")

(options, args) = parser.parse_args()
if (options.f1) and (options.f2) and (options.jobid) and (options.c1) and (options.c2) :
    print ("Start ...")
else :
    print (usage)
    print ("Not enougth arguments\n")
    quit()


# file = pd.read_csv("/Users/barradd/Desktop/PDOS_Zr-40.dat",sep='  ')
## read the file , and parse it to a list
file_list = [x.split() for x in open(options.f1).readlines() ]
## Make it a data frame
file_df =  pd.DataFrame( file_list)


### give a Header
new_header = file_df.iloc[0] #grab the first row for the header
file_df = file_df[1:] #take the data less the header row
file_df.columns = new_header #set the header row as the df header


## make the columns float type
file_df["#Energy"] = file_df["#Energy"].astype(float, copy=True)
file_df["tot"] = file_df["tot"].astype(float, copy=True)


## read the second file and process it tha same way
file_list_2 = [x.split() for x in open("/Users/barradd/Desktop/PDOS-O-119.dat").readlines() ]
file_df2 =  pd.DataFrame( file_list_2)
file_df2 = file_df2[1:]
file_df2.columns = new_header #set the header row as the df header
file_df2["#Energy"] = file_df2["#Energy"].astype(float, copy=True)
file_df2["tot"] = file_df2["tot"].astype(float, copy=True)



## Keepp columns of interest only
df_merge = pd.concat([file_df[["#Energy","tot"]], file_df2[["#Energy","tot"]]], axis=1 )

## Rename the columns at convinience
df_merge.columns = ['E1', '%s'%(options.c1), 'E2', '%s'%(options.c2)]


### Plot the values
fig, ax = plt.subplots()

df_merge.plot(x="E1",y="Zn", grid=True, xlim=(-5,5), ylim=(0,5), ax=ax)
df_merge.plot(x="E2",y="O",  grid=True, xlim=(-5,5), ylim=(0,5), style='g', ax=ax)

plt.xlabel("Energy")
plt.ylabel("DOS arbitrary units")

## save the figure with the name, on the same site
plt.savefig("%s.png"%(options.jobid),format="png",dpi=300)
