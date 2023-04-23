#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:24:12 2023

@author: ira
"""
import numpy as np
import pandas as pd
import math
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import pearsonr
from sklearn.ensemble import RandomForestRegressor
from processdata import prep_2016
from sklearn.model_selection import GridSearchCV
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
regressor = RandomForestRegressor()
rf_params = [{'max_features' : list(range(2,36))}]
clf = GridSearchCV(regressor, rf_params, cv = 10, scoring='r2', verbose=2)
clf.fit(X_train_minmax, y_train)
print("Task completed")
print("Best parameters: ", clf.best_params_)
print("Best score ", clf.best_score_)
