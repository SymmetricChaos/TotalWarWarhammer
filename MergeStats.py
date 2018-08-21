## Here we are taking the raw data from te Land_Units_Tables and Melee_Weapons+Tables
## and saving it into a Python dictionary in a usable form. Only traits we actally
## care about will be put in.

import numpy as np
import re
import linecache

## For convenience the linecache library allows us to quickly see a list of
## what traits there are and what their index is.
for i,l in enumerate(linecache.getline("Land_Units_Tables.csv",3).split("\t")):
    print(i,l)
    
for i,l in enumerate(linecache.getline("Melee_Weapons_Tables.csv",3).split("\t")):
    print(i,l)

## Open the files to read them.
stat_file = open('Land_Units_Tables.csv', 'r')
weapon_file = open('Melee_Weapons_Tables.csv', 'r')


## To start with we will take the information from Melee_Weapons_Tables and place
## it into a dictionary. The name of each key will be the name of the weapon. This
## way as we work with each unit we can select the weapon it uses and the associated
## stats.
## Note that we skip the first three lines as they contain no data we want.
weapons = dict()
for i,line in enumerate(weapon_file):
    if i > 2:
        L = line.split("\t")
        weapons[L[3]] = [L[1],L[2],L[4],L[5],L[19]]


## Prepare a dictionary to hold the information we want about each unit.
traits = ['charge','armor','category','class','melee_A','melee_D','BVL','BVI',
          'damage','ap_damage','total_damage','ap_fraction','attack_interval','name']
units = dict()
for t in traits:
    units[t] = []

## Now we will gather up the information from the Land_Units_Tables so we can
## describe each unit.
## Note that we skip the first three lines as they contain no data we want.
for i,line in enumerate(stat_file):
    if i > 2:
        # The data is separated by tabs so that is how we split it
        L = line.split("\t")
        # Armor is a bit complicated. It is stored as string with a bunch of
        # information. The actual amount of armor is the last few characters.
        # A regular expression extracts what we want then we turn it into an
        # integer
        units['armor'].append(int(re.findall("\d+$",L[1])[0]))
        
        # These stats are simply integers and all we have to do is convert them
        # to that format.
        units['charge'].append(int(L[4]))
        units['melee_A'].append(int(L[12]))
        units['melee_D'].append(int(L[13]))
        
        # These stats are best stored as strings so no change is needed.
        units['category'].append(L[3])
        units['class'].append(L[5])
        units['name'].append(L[9])

        # Now we match the unit's weapon type to the information we put into
        # the weapons dictionary we prepared earlier and put that data into it.
        weap = weapons[L[20]]
        units['BVL'].append(int(weap[0]))
        units['BVI'].append(int(weap[1]))
        units['damage'].append(int(weap[2]))
        units['ap_damage'].append(int(weap[3]))
        units['total_damage'].append(int(weap[2])+int(weap[3]))
        units['ap_fraction'].append( int(weap[3]) / (int(weap[2])+int(weap[3])))
        units['attack_interval'].append(float(re.sub("\n","",weap[4])))


np.save('unitsDictionary.npy', units)


print("Class:",np.unique(units['class']))
print("Category:",np.unique(units['category']))

print("\n\nExample of unit stats")

def read_index(n):
    for stat,val in units.items():
        print("{:<15}: {}".format(stat,val[n]))
        
read_index(161)
