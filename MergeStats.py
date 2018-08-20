import numpy as np
import re
import linecache


for i,l in enumerate(linecache.getline("Land_Units_Tables.csv",3).split("\t")):
    print(i,l)
    
for i,l in enumerate(linecache.getline("Melee_Weapons_Tables.csv",3).split("\t")):
    print(i,l)
    
stat_file = open('Land_Units_Tables.csv', 'r')
weapon_file = open('Melee_Weapons_Tables.csv', 'r')


units = dict()
weapons = dict()
units['charge'] = []
units['armor'] = []
units['category'] = []
units['class'] = []
units['melee_A'] = []
units['melee_D'] = []
units['BVL'] = []
units['BVI'] = []
units['damage'] = []
units['ap_damage'] = []
units['attack_interval'] = []
units['name'] = []



for i,line in enumerate(weapon_file):
    if i > 2:
        L = line.split("\t")
        weapons[L[3]] = [L[1],L[2],L[4],L[5],L[19]]

for i,line in enumerate(stat_file):
    if i > 2:
        L = line.split("\t")
        units['armor'].append(int(re.findall("\d+$",L[1])[0]))
        units['charge'].append(int(L[4]))
        units['category'].append(L[3])
        units['class'].append(L[5])
        units['melee_A'].append(int(L[12]))
        units['melee_D'].append(int(L[13]))
        units['name'].append(L[9])

        weap = weapons[L[20]]
        units['BVL'].append(int(weap[0]))
        units['BVI'].append(int(weap[1]))
        units['damage'].append(int(weap[2]))
        units['ap_damage'].append(int(weap[3]))
        units['attack_interval'].append(float(re.sub("\n","",weap[4])))


for stat,val in units.items():
    print(stat,val[71])

np.save('unitsDictionary.npy', units)
