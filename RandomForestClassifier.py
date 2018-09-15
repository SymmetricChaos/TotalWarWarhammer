import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

#LimitedDF = unitsDF.loc[(unitsDF['faction'] == 'brt') | (unitsDF['faction'] == 'dwf') | (unitsDF['faction'] == 'wef') | (unitsDF['faction'] == 'emp')]
LimitedDF = unitsDF.loc[(unitsDF['faction'] != 'teb') & (unitsDF['faction'] != 'ksl')]
#print(unitsDF.columns)

factors = ['armor','charge','ground_speed','melee_A','melee_D',
           'mass','leadership','shield','missile_total_damage',
           'models','ap_fraction','total_damage','fly_speed',
           'MP_cost','missile_ap_fraction']
X = LimitedDF[factors]
Y = LimitedDF['faction']


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2)


## A random forest classifier.
randforest = RandomForestClassifier(criterion = "gini",
                               max_depth=None, min_samples_leaf=1,
                               n_estimators=200)
randforest.fit(X_train, Y_train)

Y_pred = randforest.predict(X_test)

acc_scr = accuracy_score(Y_test,Y_pred)
fea_imp = randforest.feature_importances_

print("Decision Forest Accuracy {:.3f}%".format(acc_scr*100))

print("\nFeature Importance:")
for i,j in zip(factors,fea_imp):
    print("{:<20}: {:.3f}".format(i,j))


print(len(LimitedDF))
ctr = 0
print()
for i in range(len(LimitedDF)):
    if ctr > 10:
        break
    #r = np.random.randint(0,len(LimitedDF))
    x = LimitedDF[factors].iloc[i].values.reshape(1,-1)
    pred_faction = randforest.predict(x)
    true_faction = LimitedDF['faction'].iloc[i]
    
    if pred_faction[0] == true_faction:
        pass
    else:
        ctr += 1
        true_name = LimitedDF['name'].iloc[i]
        print(true_name)
        print("Predicted {}".format(pred_faction[0]))
        print("Actual    {}\n".format(true_faction))


