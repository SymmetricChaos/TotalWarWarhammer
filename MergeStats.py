import numpy as np
import matplotlib.pyplot as plt
import re

stat_file = open('UnitStats.csv', 'r')

armor = []

M = stat_file.readline()
print(M.split("\t"))

for i,line in enumerate(stat_file):
    if i > 0:
        L = line.split("\t")
        armor.append(int(re.findall("\d+$",L[0])[0]))
    
    
