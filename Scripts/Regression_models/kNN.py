#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:01:14 2023
This module uses the k nearest neighbours algorithm for regression to predict binding affinities for the taining dataset
@author: ira
"""
import numpy as np
import pandas as pd
import math
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.neighbors import KNeighborsRegressor
from processdata import prep_2016
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
knn = KNeighborsRegressor(n_neighbors=13, p=1) #the hyperparamters n_neighbours = 13 and p=1 was determined by gridsearch
knn.fit(X_train_minmax, y_train) #fitting the model
y_predict = knn.predict(X_test_minmax) #predicting y values for the test set
y_predict_train = knn.predict(X_train_minmax) #predicting y values for the training set
print("Size of y_test ", np.size(y_predict))
print("Size of y_predict ", np.size(y_predict)) #these should match
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
plt.title("kNN Regressor")
plt.show()
residuals = np.subtract(y_predict, y_test)
plt.scatter(y_predict,residuals)
plt.xlabel('Predicted binding affinities')
plt.ylabel('Residuals')
plt.title('Residuals vs predicted binding affinities for kNN regressor')
plt.show
