#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:01:38 2023
This file performs a randomized search of the hyperparameter space for the SVR
@author: ira
"""
import numpy as np
import pandas as pd
import math
from sklearn.svm import SVR
from processdata import prep_2016
from sklearn.model_selection import RandomizedSearchCV
gamma_values = []
epsilon_values = []
C_values = []

def param_space(e1,e2,e3): #this function generates the hyperparameter space. e1, e2, e3 are the range of exponents for base 2
    for i in range(e1[0], e1[1]):
        epsilon_values.append(2**i)
    print("Epsilon values :", epsilon_values)
    for i in range(e2[0], e2[1]):
        gamma_values.append(2**i)
    print("Gamma values: ", gamma_values)
    for i in range(e3[0], e3[1]):
        C_values.append(2**i)
    print("C values: ", C_values)
    param_values = [{'gamma':gamma_values,'epsilon':epsilon_values,'C':C_values}]
    return param_values

temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
regressor = SVR()
svr_params = param_space([-5,2], [-5,2], [-10,10])
clf = RandomizedSearchCV(regressor, svr_params, cv = 10, scoring='r2', verbose=2, random_state=42)
clf.fit(X_train_minmax, y_train)
print("Task completed")
print("Best parameters: ", clf.best_params_)
print("Best score ", clf.best_score_)
