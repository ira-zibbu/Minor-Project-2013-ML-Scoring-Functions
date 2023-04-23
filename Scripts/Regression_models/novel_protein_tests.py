#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:23:10 2023
This file tests the scoring ad ranking power of the 5 ML models on the unseen protein carbonic anhydrase, HIV protease and trypsin
@author: ira
"""
import numpy as np
import pandas as pd
from sklearn import linear_model
from pyearth import Earth
from scipy.stats import spearmanr, kendalltau, pearsonr
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import math
from processdata import process_HIV_protease, process_carbonic_anhydrase, process_trypsin
import os
import matplotlib.pyplot as plt
Results = []

def model_metrics_generate(y_test, y_predict, y_train, y_predict_train): #adds model performance mectrics to Results
    Results.append("Pearson Correlation coefficient between y_test and y_predict: " + str(pearsonr(y_test, y_predict)) + "\n") #pearson correlation coefficient
    MSE = mean_squared_error(y_test, y_predict)
    RMSE = math.sqrt(MSE)
    Results.append("Root Mean Square Error on the testing set: " + str(RMSE)+ "\n")
    MSE = mean_squared_error(y_train, y_predict_train)
    RMSE = math.sqrt(MSE)
    Results.append("Root Mean Square Error on the training set: " + str(RMSE)+ "\n")
    Results.append("Coefficient of determination: "+ str(r2_score(y_test,y_predict))+ "\n")
    spearman_coeff = spearmanr(y_test,y_predict)
    kendall_coeff = kendalltau(y_test, y_predict)
    Results.append("Spearman rank correlation coefficient between y_test and y_predict : " + str(spearman_coeff)+ "\n")
    Results.append("Kendall tau rank correlation coefficient between y_test and y_predict : " + str(kendall_coeff) + "\n")
    
def make_scatter_plot(prot_name, model_name, y_test, y_predict, plot_title): #produces a scatter plot of predicted vs expt values
    os.chdir("/home/ira/Desktop/Minor Project/Results/novel_protein_test")
    file_name = prot_name + "_" + model_name + "_scatter.png"
    plt.scatter(y_test, y_predict)
    plt.xlabel("Test binding affinities")
    plt.ylabel("Predicted binding affinities")
    plt.title(plot_title + " on " + prot_name + " test set")
    plt.show()
    plt.savefig(file_name)

## Linear model
def linear_regression_model(X_train_minmax, y_train, X_test_minmax,y_test, prot_name):
    Results.append("LINEAR REGRESSION \n")
    model_r = linear_model.LinearRegression() #applying linear regression 
    model_r.fit(X_train_minmax,y_train)
    #("coefficients = " , model_r.coef_) #coefficients of the scoring functions
    #('intercepts = ' , model_r.intercept_) #y intercept of the scoring function
    y_predict = model_r.predict(X_test_minmax) #predicting binding affinity for the test data
    y_predict_train = model_r.predict(X_train_minmax) #predicting binding affinity for the training data
    model_metrics_generate(y_test, y_predict, y_train, y_predict_train)
    make_scatter_plot(prot_name, "linear_regression", y_test, y_predict, "Linear regression")
    
def MARS_model(X_train_minmax, y_train, X_test_minmax,y_test, prot_name):
    Results.append("MARS \n")
    model_r = Earth(penalty = 5, max_degree = 1)
    model_r.fit(X_train_minmax,y_train)
    #print("Model coefficients = " , model_r.coef_) #coefficients of the scoring functions
    y_predict_train = model_r.predict(X_train_minmax)
    y_predict = model_r.predict(X_test_minmax) #predicting binding affinity for the input data
    model_metrics_generate(y_test, y_predict, y_train, y_predict_train)
    make_scatter_plot(prot_name, "MARS", y_test, y_predict, "MARS")
    
def kNN_model(X_train_minmax, y_train, X_test_minmax,y_test, prot_name):
    Results.append("kNN \n")
    knn = KNeighborsRegressor(n_neighbors=13, p=1) #the hyperparamters n_neighbours = 13 and p=1 was determined by gridsearch
    knn.fit(X_train_minmax, y_train) #fitting the model
    y_predict = knn.predict(X_test_minmax) #predicting y values for the test set
    y_predict_train = knn.predict(X_train_minmax) #predicting y values for the training set
    model_metrics_generate(y_test, y_predict, y_train, y_predict_train)
    make_scatter_plot(prot_name, "kNN", y_test, y_predict, "kNN")


def SVR_model(X_train_minmax, y_train, X_test_minmax,y_test, prot_name):
    Results.append("Support vector machine regression \n")
    regressor = SVR(kernel = 'rbf', gamma = 0.125, epsilon=0.25, C=1)
    regressor.fit(X_train_minmax, y_train)
    y_predict = regressor.predict(X_test_minmax)
    y_predict_train = regressor.predict(X_train_minmax)
    model_metrics_generate(y_test, y_predict, y_train, y_predict_train)
    make_scatter_plot(prot_name, "SVM_regression", y_test, y_predict, "SVM regression")
    
def RF_model(X_train_minmax, y_train, X_test_minmax,y_test, prot_name):
    Results.append("Random forest regression \n")
    regressor = RandomForestRegressor(n_estimators=2000, max_features=2) #best max_features for 2016 set is 2, as determined by grid search
    regressor.fit(X_train_minmax, y_train)
    y_predict = regressor.predict(X_test_minmax)
    y_predict_train= regressor.predict(X_train_minmax)
    model_metrics_generate(y_test, y_predict, y_train, y_predict_train)
    make_scatter_plot(prot_name, "RF", y_test, y_predict, "Random forest")

def run_models(X_train_minmax, y_train, X_test_minmax,y_test,prot_name):
    linear_regression_model(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
    MARS_model(X_train_minmax, y_train, X_test_minmax,y_test, prot_name)
    kNN_model(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
    SVR_model(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
    RF_model(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
   

#HIV PROTEASE
Results.append("HIV PROTEASE \n")
prot_name = "HIV protease"
temp = process_HIV_protease() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
run_models(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
print("HIV protease complete")

#CARBONIC ANHYDRASE
Results.append("CARBONIC ANHYDRASE \n")
prot_name = "Carbonic anhydrase"
temp = process_carbonic_anhydrase() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
run_models(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
print("Carbonic anhydrase complete")

#TRYPSIN
Results.append("TRYPSIN \n")
prot_name = "trypsin"
temp = process_trypsin() #loading the normalized training and test dataset
X_train_minmax = temp[0] #normalized training dataset
y_train = temp[1] #BA of the training set
X_test_minmax = temp[2] #normalized testing data set
y_test = temp[3] #BA of the testing dataset
run_models(X_train_minmax, y_train, X_test_minmax,y_test,prot_name)
print("Trypsin complete")

os.chdir("/home/ira/Desktop/Minor Project/Results")
file = open("results_novel_proteins.txt",'w')
file.writelines(Results)
file.close()		
 
