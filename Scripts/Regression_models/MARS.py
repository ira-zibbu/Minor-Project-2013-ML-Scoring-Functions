#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:26:31 2023
This file uses a multivariate adaptive regression splines (MARS) model 
@author: ira
"""
#This module performs multivariate adaptive regression splines (MARS) on the feature sets. It provides the pearson correlation
#coefficient and RMSE between the predicted and actual values of the testing data set
import numpy as np
import pandas as pd
import math
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from pyearth import Earth
from processdata import prep_2016
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
model_r = Earth(penalty = 5, max_degree = 1)
model_r.fit(X_train_minmax,y_train)
print("Model coefficients = " , model_r.coef_) #coefficients of the scoring functions
y_predict_train = model_r.predict(X_train_minmax)
y_predict = model_r.predict(X_test_minmax) #predicting binding affinity for the input data
print("Last predicted BAs ", y_predict[-4:-1])
print("Size of y_test ", np.size(y_predict))
print("Size of y_predict ", np.size(y_predict))
print("Correlation coefficient is: " , pearsonr(y_test, y_predict)) #pearson correlation coefficient
MSE = mean_squared_error(y_test, y_predict)
RMSE = math.sqrt(MSE)
print("Root Mean Square Error on the testing set:", RMSE)
MSE = mean_squared_error(y_train, y_predict_train)
RMSE = math.sqrt(MSE)
print("Root Mean Square Error on the training set:", RMSE)
print("Coefficient of determination: ", r2_score(y_test,y_predict))
plt.scatter(y_test, y_predict)
plt.xlabel("Test binding affinities")
plt.ylabel("Predicted binding affinities")
plt.title("MARS")
plt.show()
residuals = np.subtract(y_predict, y_test)
plt.scatter(y_predict,residuals)
plt.xlabel('Predicted binding affinities')
plt.ylabel('Residuals')
plt.title('Residuals vs predicted binding affinities for MARS')
plt.show
