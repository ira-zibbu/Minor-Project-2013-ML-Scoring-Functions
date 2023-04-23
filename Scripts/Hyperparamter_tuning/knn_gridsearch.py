#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:46:17 2023
This script performs a grid search of possible paramters for kNN
@author: ira
"""
import numpy as np
import pandas as pd
import math
from sklearn.neighbors import KNeighborsRegressor
from processdata import prep_2016
from sklearn.model_selection import GridSearchCV
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
knn = KNeighborsRegressor()
knn_params = [{'n_neighbors': list(range(1,30)), 'p': list(range(1,4))}] #defining the parameter space
clf = GridSearchCV(knn, knn_params, cv = 10, scoring='r2', verbose=2)
clf.fit(X_train_minmax, y_train)
print("Task completed")
print("Best parameters: ", clf.best_params_)
print("Best score ", clf.best_score_)
