import numpy as np
import matplotlib.pyplot as plt
import pickle

units = pickle.load( open( "unitsDict.p", "rb" ) )

def histoplot(L,bins,x_ticks,size=[13,6],title=""):
    
    
    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    plt.hist(L,bins=bins)
    plt.xticks(x_ticks)
    plt.title(title,size=20)
    percentiles = np.percentile(L,[20,50,80])
    for x in percentiles:
        plt.axvline(x,color='black',linewidth=3)
    percentile_legend = []
    for i,j in zip(['20','50','80'],percentiles):
         percentile_legend.append("{}th Percentile: {:.1f}".format(i,j))
    plt.legend(percentile_legend)
    plt.show()


histoplot(units['armor'],np.arange(0,210,10),[i*10 for i in range(0,21)],[13,6],
          "Armor Distribution\nWith 20th, 50th, 80th Percentiles")


histoplot(units['melee_A'],np.arange(0,105,5),[i*5 for i in range(0,21)],[13,6],
          "Melee Attack Distribution\nWith 20th, 50th, 80th Percentiles")

histoplot(units['melee_D'],np.arange(0,105,5),[i*5 for i in range(0,21)],[13,6],
          "Melee Defense Distribution\nWith 20th, 50th, 80th Percentiles")

histoplot(units['total_damage'],np.arange(0,600,20),[i*20 for i in range(0,31)],[13,6],
          "Total Damage Distribution\nWith 20th, 50th, 80th Percentiles")


L = []
for dam,cla in zip(units['total_damage'],units['class']):
    if cla != 'com':
        L.append(dam)

histoplot(L,np.arange(0,600,20),[i*20 for i in range(0,31)],[13,6],
          "Total Damage Distribution (No Lords or Heroes)\nWith 20th, 50th, 80th Percentiles")

histoplot(units['ap_fraction'],np.linspace(0,1,21),np.linspace(0,1,21),[13,6],
          "AP Fraction Distribution\nWith 20th, 50th, 80th Percentiles")




    