import numpy as np
import matplotlib.pyplot as plt


units = np.load('unitsDictionary.npy').item()

def hit_prob(A,D):
    r = 35+A-D
    h = min(max(r,8),90)
    return h/100

def armor_resist(armor):
    ar = np.linspace(armor/2,armor)
    ar = [min(x,100) for x in ar]
    return np.mean(ar)/100

def average_damage(armor,normal_damage,ap_damage,MA,MD):
    hit = hit_prob(MA,MD)
    norma_res = armor_resist(armor)
    return ((normal_damage*(1-norma_res))+ap_damage)*hit
    

def read_index(n):
    for stat,val in units.items():
        print("{:<15}: {}".format(stat,val[n]))

eternal_guard = units['name'].index("wh_dlc05_wef_inf_eternal_guard_0")
crypt_ghouls = units['name'].index("wh_main_vmp_inf_crypt_ghouls")

read_index(eternal_guard)
print("\n")
read_index(crypt_ghouls)

print("\n\n")
print("Eternal Guard",average_damage(80,4,20,26,30))
print("Crypt Ghouls ",average_damage(80,36,4,27,30))

EG = []
CG = []
for i in range(0,201):
    EG.append(average_damage(i,4,20,26,MD=32))
    CG.append(average_damage(i,36,4,27,MD=32))

plt.figure()
plt.gcf().set_size_inches(12, 6)
plt.plot(EG)
plt.plot(CG)
plt.legend(["Eternal Guard","Crypt Ghouls"])
plt.ylabel("Average Damage")
plt.xlabel("Armor")
plt.xticks(np.arange(0,210,10))
plt.title("Average Damage vs Unit with MD=32",size=20)
plt.grid()