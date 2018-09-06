import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



unitsDF = pickle.load( open( "unitsDF.p", "rb" ) )

LimitedDF = unitsDF.loc[(unitsDF['faction'] == 'brt') | (unitsDF['faction'] == 'dwf') | (unitsDF['faction'] == 'wef') | (unitsDF['faction'] == 'emp')]

#print(unitsDF.columns)

factors = ['armor','charge','ground_speed','melee_A','melee_D','mass','leadership']
X = LimitedDF[factors]
Y = LimitedDF['faction']

best_acc = 0
trials = 20
for i in range(trials):

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.3)
    
    
    ## An ordinary decision tree
    randforest = RandomForestClassifier(criterion = "gini",
                                   max_depth=None, min_samples_leaf=1,
                                   n_estimators=200)
    randforest.fit(X_train, Y_train)
    
    Y_pred = randforest.predict(X_test)
    
    acc_scr = accuracy_score(Y_test,Y_pred)
    avg_acc += acc_scr/trials
    avg_imp += randforest.feature_importances_/trials

print("Mean Decision Forest Accuracy {:.3f}%".format(avg_acc*100))

print("\nAverage Feature Importance:")
for i,j in zip(factors,avg_imp):
    print("{:<14}: {:.3f}".format(i,j))