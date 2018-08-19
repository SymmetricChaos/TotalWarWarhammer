import numpy as np
import matplotlib.pyplot as plt

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


def hit_prob(A,D):
    r = 35+A-D
    h = min(max(r,8),90)
    return h/100

def armor_resist(armor)
    ar = np.linspace(i/2,i)
    ar = [min(x,100) for x in ar]
    return np.mean(ar)/100

def average_damage(armor,normal_damage,ap_damage,MA,MD):


x = np.arange(-55,28,1)
y = []
for i in x:
    y.append(hit_prob(100,100+i))
y = np.array(y)
plt.plot(x,y)
plt.ylabel("Hit Probability")
plt.xlabel("Difference Between MA and MD")