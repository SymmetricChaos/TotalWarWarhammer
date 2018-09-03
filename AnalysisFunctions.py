import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd

def histoplot(L,bins,x_ticks,size=[13,6],title="",stacked=True,ranks=[20,50,80]):
    

    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    H = plt.hist(L,bins=bins,stacked=stacked)
    plt.xticks(x_ticks)
    plt.title(title,size=20)

    if ranks == []:
        pass
    else:
        percentiles = np.percentile(L,ranks)
        for x in percentiles:
            plt.axvline(x,color='black',linewidth=3)
        percentile_legend = []
        for i,j in zip([str(r) for r in ranks],percentiles):
             percentile_legend.append("{}th Percentile: {:.1f}".format(i,j))
        plt.legend(percentile_legend)
    
    return H