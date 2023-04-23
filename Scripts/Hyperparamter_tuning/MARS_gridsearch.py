#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:59:28 2023
This script performs a grid search of the parameter space of the hyperparamter 'penalty' and 'degree' for the MARS model
The parameter space for 'penalty' is [0,30] and for degree it is [0,5]. 
@author: ira
"""
import numpy as np
import pandas as pd
import math
from pyearth import Earth
from processdata import prep_2016
from sklearn.model_selection import GridSearchCV
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
model_r = Earth()
earth_params = [{'penalty': list(range(0,15)), 'max_degree': list(range(1,5))}]
clf = GridSearchCV(model_r, earth_params, cv = 10, scoring='r2', verbose = 2)
clf.fit(X_train_minmax, y_train)
print("Task completed")
print("Best parameteres: ", clf.best_params_)
print("Best score ", clf.best_score_)