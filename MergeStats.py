## Here we are taking the raw data from te Land_Units_Tables and Melee_Weapons+Tables
## and saving it into a Python dictionary in a usable form. Only traits we actally
## care about will be put in.

import numpy as np
import re
import linecache
import pandas as pd 
import pickle

## For convenience the linecache library allows us to quickly see a list of
## what traits there are and what their index is.
#for i,l in enumerate(linecache.getline("Land_Units_Tables.csv",3).split("\t")):
#    print(i,l)
    
#for i,l in enumerate(linecache.getline("Melee_Weapons_Tables.csv",3).split("\t")):
#    print(i,l)
    
for i,l in enumerate(linecache.getline("Main_Units_Tables.csv",3).split("\t")):
    print(i,l)

#for i,l in enumerate(linecache.getline("Battle_Entities_Tables.csv",3).split("\t")):
#    print(i,l)

## Open the files to read them.
stat_file = open('Land_Units_Tables.csv', 'r')
weapon_file = open('Melee_Weapons_Tables.csv', 'r')
names_file = open('OnscreenNames.csv', 'r')
main_units_file = open('Main_Units_Tables.csv', 'r')
battle_entities_file = open('Battle_Entities_Tables.csv', 'r')
mounts_tables_file = open('Mounts_Tables.csv', 'r')

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
    
## Here we take in the data from the OnscreeNames file  
names = dict()
for i,line in enumerate(names_file):
    L = line.split("\t")
    if "_onscreen_" in L[0]:
        kn = re.sub("land_units_onscreen_name_","",L[0])
        names[kn] = L[1][1:-1]
        
## Here we take in the data from the Main_Units_Tables file
## For some insane reason there are a number of dummied out naval units on
## this list that share a land_unit keyname with actual units in the game. We
## filter them out.
main = dict()
for i,line in enumerate(main_units_file):
    if i > 2:
        L = line.split("\t")
        if "_shp_" not in L[17]:
            main[L[5]] = [L[2],L[6],L[19],L[8]]
            
entities = dict()
for i,line in enumerate(battle_entities_file):
    if i > 2:
        L = line.split("\t")
        entities[L[0]] = L[17]
        
mounts = dict()
for i,line in enumerate(mounts_tables_file):
    if i > 2:
        L = line.split("\t")
        entities[L[0]] = L[2]
        
     
## Prepare a dictionary to hold the information we want about each unit.
traits = ['name','key_name','charge','armor','category','class','melee_A','melee_D',
          'BVL','BVI','damage','ap_damage','total_damage','ap_fraction',
          'attack_interval','faction','caste','models','weight_class','melee_weapon',
          'leadership','missile_weapon','MP_cost']
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
        units['leadership'].append(int(L[14]))

        ## Calculuating HP turns out to be really hard.
        #num_mounts = int(L[19])
        #num_engines = int(L[51])
        #if L[16] == "":
        #    mount_hp = 0
        #else:
        #    mount_hp = entities[mounts[L[16]]]
        #if L[31] == "":
        #    engine_hp = 0
        #else:
        #    engine_hp = entities[mounts[L[31]]]  
        
        #if "settra" in L[9]:
        #    print(L[19],L[51])
        #    print(L[16],"  ",L[31])
        #    print(mount_hp," ",engine_hp)
            
        
        # These stats are best stored as strings so no change is needed.
        units['category'].append(L[3])
        units['class'].append(L[5])
        units['key_name'].append(L[9])
        units['melee_weapon'].append(L[20])
        units['missile_weapon'].append(L[21])
        
        # Now we make use of the keyname to link to information in other
        # dictionaries we created.
        units['name'].append(names['"'+L[9]+'"'])
        
        additional = main[L[9]]
        units['caste'].append(additional[0])
        # Models are converted to the standard 75% large size
        units['models'].append(int(np.ceil(float(additional[1])*.75)))
        units['weight_class'].append(additional[2])
        units['MP_cost'].append(int(additional[3]))

        # Finally we can use the keyname to get the faction that the unit belongs
        # to
        fct = L[9].split("_")
        units['faction'].append(fct[2])

        # Now we match the unit's weapon type to the information we put into
        # the weapons dictionary we prepared earlier and put that data into it.
        weap = weapons[L[20]]
        units['BVL'].append(int(weap[0]))
        units['BVI'].append(int(weap[1]))
        units['damage'].append(int(weap[2]))
        units['ap_damage'].append(int(weap[3]))
        units['total_damage'].append(int(weap[2])+int(weap[3]))
        units['ap_fraction'].append( int(weap[3]) / (int(weap[2])+int(weap[3])))
        
        # Attack interval is at the end of a line so we need to remove the
        # newline marker and then convert to a floating point number
        units['attack_interval'].append(float(re.sub("\n","",weap[4])))
        
        

unitsDF = pd.DataFrame(units)
pd.set_option('display.max_columns', 500)
#for i in ['caste','category','class','faction']:
#    print("{}: {}\n".format(i,unitsDF[i].unique()))

#print(unitsDF.columns.tolist())
pickle.dump(unitsDF, open( "unitsDF.p", "wb" ) )
pickle.dump(units, open( "unitsDict.p", "wb" ) )

print(unitsDF.loc[unitsDF['key_name'].str.contains('_orion')])
