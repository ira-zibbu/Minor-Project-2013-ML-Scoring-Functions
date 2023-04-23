#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:06:38 2023

@author: ira
"""
import numpy as np
import pandas as pd
import math
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.ensemble import RandomForestRegressor
from processdata import prep_2016
temp = prep_2016() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
regressor = RandomForestRegressor(n_estimators=2000, max_features=2) #best max_features for 2016 set is 2, as determined by grid search
regressor.fit(X_train_minmax, y_train)
y_predict = regressor.predict(X_test_minmax)
y_predict_train= regressor.predict(X_train_minmax)
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
plt.title("Random Forest")
plt.show()
residuals = np.subtract(y_predict, y_test)
plt.scatter(y_predict,residuals)
plt.xlabel('Predicted binding affinities')
plt.ylabel('Residuals')
plt.title('Residuals vs predicted binding affinities for random forest')
plt.show
