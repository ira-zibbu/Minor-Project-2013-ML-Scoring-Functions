#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:33:31 2023
This module performs support vector regression on the training set, and outputs a scatter plot of the test vs predicted binding
affinities, the pearson correlation coefficient
@author: ira
"""
import numpy as np
import pandas as pd
import math
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.svm import SVR
from processdata import prep_2016
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
regressor = SVR(kernel = 'rbf', gamma = 0.125, epsilon=0.25, C=1)
regressor.fit(X_train_minmax, y_train)
y_predict = regressor.predict(X_test_minmax)
y_predict_train = regressor.predict(X_train_minmax)
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
plt.title("Support Vector Regression")
plt.show()
residuals = np.subtract(y_predict, y_test)
plt.scatter(y_predict,residuals)
plt.xlabel('Predicted binding affinities')
plt.ylabel('Residuals')
plt.title('Residuals vs predicted binding affinities for support vector regression')
plt.show

