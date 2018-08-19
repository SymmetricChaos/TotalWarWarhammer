import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

stat_file = open('WarhammerUnitStats.csv', 'r')

armor, charge, meleeA, meleeD, morale = [],[],[],[],[]

for i,line in enumerate(stat_file):
    if i > 0: 
        a,b,c,d,e = line.split("\t")
        armor.append(int(a))
        charge.append(int(b))
        meleeA.append(int(c))
        meleeD.append(int(d))
        morale.append(int(e))

meleeA = np.array(meleeA)
charge = np.array(charge)
meleeD = np.array(meleeD)
armor  = np.array(armor)
morale = np.array(morale)

percentiles = [20,50,80]

fig = plt.figure()
fig.set_size_inches(12, 6)
x_ticks = [i*10 for i in range(0,21)]
plt.hist(armor,bins=np.arange(0,210,10))
plt.xticks(x_ticks)
plt.title("Armor Distribution\nWith 20th, 50th, 80th Percentiles",size=20)
for x in np.percentile(armor,percentiles):
    plt.axvline(x,color='black',linewidth=4)
#plt.yticks([])
plt.show()



fig = plt.figure()
fig.set_size_inches(12, 6)
x_ticks = [i*5 for i in range(0,21)]
plt.hist(meleeA,bins=np.arange(0,105,5))
plt.xticks(x_ticks)
plt.title("Melee Attack Distribution\nWith 20th, 50th, 80th Percentiles",size=20)
for x in np.percentile(meleeA,percentiles):
    plt.axvline(x,color='black',linewidth=4)
#plt.yticks([])
plt.show()



fig = plt.figure()
fig.set_size_inches(12, 6)
x_ticks = [i*5 for i in range(0,21)]
plt.hist(meleeD,bins=np.arange(0,105,5))
plt.xticks(x_ticks)
plt.title("Melee Defense Distribution\nWith 20th, 50th, 80th Percentiles",size=20)
for x in np.percentile(meleeD,percentiles):
    plt.axvline(x,color='black',linewidth=4)
#plt.yticks([])
plt.show()