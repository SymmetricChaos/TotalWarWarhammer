import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )
unitswithcost = unitsDF.loc[unitsDF['faction'] != 'tmb']

mod = linear_model.LinearRegression()


MP_cost = unitswithcost['MP_cost'].values.reshape(-1,1)

X = []
for i in ['melee_A','melee_D','leadership','damage','ap_damage','armor','charge']:
    X.append(unitswithcost[i].values)

X = np.array(X).T



mod.fit(X,MP_cost)

predicted_MP_cost = mod.predict(X)

print(mod.coef_)
print(mean_squared_error(MP_cost, predicted_MP_cost))
print(r2_score(MP_cost, predicted_MP_cost))

#plt.scatter(leadership,MP_cost)
#plt.plot(leadership,predicted_MP_cost,
#            color='red')