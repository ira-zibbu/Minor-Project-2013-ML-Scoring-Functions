
"""
Created on Mon Mar 20 22:49:01 2023
This module can be called from the other scripts. It returns the training and test data sets by extracting them as
np arrays and normalizing X matrices. 
@author: ira
"""
import numpy as np
import pandas as pd
from sklearn import preprocessing
from random import randint
def prep_process (FILENAME1, FILENAME2): 
    df_train = pd.read_csv(FILENAME1) #dataframe of the training data
    df_test = pd.read_csv(FILENAME2) #dataframe of the testing data
    #print("Dimension of the training set dataframe = ", df_train.shape)
    #print("Dimension of the testing set dataframe = ", df_test.shape)
    #this df has 1st column as BA, columns 2-82 as the occurence count and the last column as PDB ID
    #the number of rows is the number of complexes
    drop_protein_num = ['9','15','17','35','53'] #atomic number of elements not found in proteins
    all_at_num = ['6','7','8','9','15','16','17','35','53'] #atomic number of all atoms in consideration
    drop_column_list = [] #will store the names of columns that need to be dropped. The names are in the format 'n.m' where n the at no. the protein 
    for  i in drop_protein_num:
        for j in all_at_num:
            drop_column_list.append(i+'.'+j)
    #print("the number of columns being dropped is = ", len(drop_column_list)) 
    df_train1 = df_train.drop(columns = ['9.6', '9.7', '9.8', '9.9', '9.15', '9.16', '9.17', '9.35', '9.53', '15.6', '15.7', '15.8', '15.9', '15.15', '15.16', '15.17', '15.35', '15.53', '17.6', '17.7', '17.8', '17.9', '17.15', '17.16', '17.17', '17.35', '17.53', '35.6', '35.7', '35.8', '35.9', '35.15', '35.16', '35.17', '35.35', '35.53', '53.6', '53.7', '53.8', '53.9', '53.15', '53.16', '53.17', '53.35', '53.53'])
    df_test1 = df_test.drop(columns = ['9.6', '9.7', '9.8', '9.9', '9.15', '9.16', '9.17', '9.35', '9.53', '15.6', '15.7', '15.8', '15.9', '15.15', '15.16', '15.17', '15.35', '15.53', '17.6', '17.7', '17.8', '17.9', '17.15', '17.16', '17.17', '17.35', '17.53', '35.6', '35.7', '35.8', '35.9', '35.15', '35.16', '35.17', '35.35', '35.53', '53.6', '53.7', '53.8', '53.9', '53.15', '53.16', '53.17', '53.35', '53.53'])
    #print("Dimension of the training set after reducing dimensions = ", df_train1.shape)
    #print("Dimension of the testing set after reducing dimensions= ", df_test1.shape)
    #print("Training dataset")
    #print(df_train1.head()) #print the first 5 rows of the dataset
    #print("Testing dataset")
    #print(df_test1.head()) #print the first 5 rows of the data set
    y_train = df_train1.values[:,0] #stores the first column, which are the BA
    X_train = df_train1.values[:, 1:37] #stores the occurence counts of all complexes
    y_test = df_test1.values[:, 0] #stores the first column, which are the BA
    X_test = df_test1.values[:, 1:37] #stores the occurence counts of all complexes
    print("The dimensions of X_train np array: ", X_train.shape)
    print("The dimensions of X_test np array: ", X_test.shape)
    #print(X_train[-3:-1]) #check back on this for some reason the last row of the csv file isnt read
    #print(y[-3:-1])
    #print(type(X_train)) #X is an nparray
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_minxmax = min_max_scaler.fit_transform(X_train) #scaling the data to range 0-1
    min_max_scaler = preprocessing.MinMaxScaler()
    X_test_minxmax = min_max_scaler.fit_transform(X_test) #scaling the data to range 0-1
    #print("Scaled X_train ", X_train_minxmax[-3:-1])
    #print("Scaled X_test ", X_test_minxmax[-3:-1])
    return [X_train_minxmax, y_train, X_test_minxmax, y_test]

def random_subset(subset_size): #this function will return a subset of size subset_size samples of the training set
    FILENAME2 = '/home/ira/Desktop/Minor Project/Featuresets/CASF_coreset2016.csv' #add the full path length of the index file of the testing data set
    FILENAME1 = '/home/ira/Desktop/Minor Project/Featuresets/PDBbind_trainingset_2016.csv' #the full path of the training dataset
    df_train = pd.read_csv(FILENAME1) #dataframe of the training data
    df_test = pd.read_csv(FILENAME2) #dataframe of the testing data
    #this df has 1st column as BA, columns 2-82 as the occurence count and the last column as PDB ID
    #the number of rows is the number of complexes
    drop_protein_num = ['9','15','17','35','53'] #atomic number of elements not found in proteins
    all_at_num = ['6','7','8','9','15','16','17','35','53'] #atomic number of all atoms in consideration
    drop_column_list = [] #will store the names of columns that need to be dropped. The names are in the format 'n.m' where n the at no. the protein 
    for  i in drop_protein_num:
        for j in all_at_num:
            drop_column_list.append(i+'.'+j)
    df_train1 = df_train.drop(columns = ['9.6', '9.7', '9.8', '9.9', '9.15', '9.16', '9.17', '9.35', '9.53', '15.6', '15.7', '15.8', '15.9', '15.15', '15.16', '15.17', '15.35', '15.53', '17.6', '17.7', '17.8', '17.9', '17.15', '17.16', '17.17', '17.35', '17.53', '35.6', '35.7', '35.8', '35.9', '35.15', '35.16', '35.17', '35.35', '35.53', '53.6', '53.7', '53.8', '53.9', '53.15', '53.16', '53.17', '53.35', '53.53'])
    df_test1 = df_test.drop(columns = ['9.6', '9.7', '9.8', '9.9', '9.15', '9.16', '9.17', '9.35', '9.53', '15.6', '15.7', '15.8', '15.9', '15.15', '15.16', '15.17', '15.35', '15.53', '17.6', '17.7', '17.8', '17.9', '17.15', '17.16', '17.17', '17.35', '17.53', '35.6', '35.7', '35.8', '35.9', '35.15', '35.16', '35.17', '35.35', '35.53', '53.6', '53.7', '53.8', '53.9', '53.15', '53.16', '53.17', '53.35', '53.53'])
    random_number = randint(1,100)
    df_train_subset = df_train1.sample(n = subset_size, replace = False, random_state = random_number) #creates a subset of size of subset_size samples and stores it another dataframe
    y_train = df_train_subset.values[:,0] #stores the first column, which are the BA
    X_train = df_train_subset.values[:, 1:37] #stores the occurence counts of all complexes
    y_test = df_test1.values[:, 0] #stores the first column, which are the BA
    X_test = df_test1.values[:, 1:37] #stores the occurence counts of all complexes
    #print("The dimensions of X_train np array: ", X_train.shape)
    #print("The dimensions of X_test np array: ", X_test.shape)
    #print(X_train[-3:-1]) #check back on this for some reason the last row of the csv file isnt read
    #print(y[-3:-1])
    #print(type(X_train)) #X is an nparray
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_minxmax = min_max_scaler.fit_transform(X_train) #scaling the data to range 0-1
    min_max_scaler = preprocessing.MinMaxScaler()
    X_test_minxmax = min_max_scaler.fit_transform(X_test) #scaling the data to range 0-1
    return [X_train_minxmax, y_train, X_test_minxmax, y_test]                                   
    
def prep_2007 (): #this function returns np arrays of the training and test data for 2007 dataset
    FILENAME1 = '/home/ira/Desktop/Minor Project/Featuresets/PDBbind_refined07-core07.csv' #add the full path length of csv file of feature set of training data
    FILENAME2 = '/home/ira/Desktop/Minor Project/Featuresets/PDBbind_core07.csv' #tadd the full path length of the csv file of the feature set of the testing data
    op = prep_process(FILENAME1, FILENAME2)
    return op
    

def prep_2016(): #returns the np arrays of the training and test data for the 2016 dataset
    FILENAME2 = '/home/ira/Desktop/Minor Project/Featuresets/CASF_coreset2016.csv' #add the full path length of the index file of the training set
    FILENAME1 = '/home/ira/Desktop/Minor Project/Featuresets/PDBbind_trainingset_2016.csv' #the testing dataset
    op = prep_process(FILENAME1, FILENAME2)
    return op

def process_clusters(CLUSTER_FILENAME): #returns np array of the test data set of the ith cluster
    df_test = pd.read_csv(CLUSTER_FILENAME) #dataframe of the testing data
    df_test = df_test.sort_values(by=['pbindaff'])
    print("Sorted dataframe of cluster = ", df_test)
    #print("Dimension of the testing set dataframe = ", df_test.shape)
    #this df has 1st column as BA, columns 2-82 as the occurence count and the last column as PDB ID
    #the number of rows is the number of complexes
    drop_protein_num = ['9','15','17','35','53'] #atomic number of elements not found in proteins
    all_at_num = ['6','7','8','9','15','16','17','35','53'] #atomic number of all atoms in consideration
    drop_column_list = [] #will store the names of columns that need to be dropped. The names are in the format 'n.m' where n the at no. the protein 
    for  i in drop_protein_num:
        for j in all_at_num:
            drop_column_list.append(i+'.'+j)
   #print("the number of columns being dropped is = ", len(drop_column_list)) 
    df_test1 = df_test.drop(columns = ['9.6', '9.7', '9.8', '9.9', '9.15', '9.16', '9.17', '9.35', '9.53', '15.6', '15.7', '15.8', '15.9', '15.15', '15.16', '15.17', '15.35', '15.53', '17.6', '17.7', '17.8', '17.9', '17.15', '17.16', '17.17', '17.35', '17.53', '35.6', '35.7', '35.8', '35.9', '35.15', '35.16', '35.17', '35.35', '35.53', '53.6', '53.7', '53.8', '53.9', '53.15', '53.16', '53.17', '53.35', '53.53'])
    #print("Dimension of the testing set after reducing dimensions= ", df_test1.shape)
    y_test = df_test1.values[:, 0] #stores the first column, which are the BA
    X_test = df_test1.values[:, 1:37] #stores the occurence counts of all complexes
    #print("The dimensions of X_test np array: ", X_test.shape)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_test_minxmax = min_max_scaler.fit_transform(X_test) #scaling the data to range 0-1
    return [X_test_minxmax, y_test]

def process_trainingset_2016(TRAINING_FILENAME):
    df_train = pd.read_csv(TRAINING_FILENAME) #dataframe of the training data
    print("Dimension of the training set dataframe = ", df_train.shape)
    #this df has 1st column as BA, columns 2-82 as the occurence count and the last column as PDB ID
    #the number of rows is the number of complexes
    drop_protein_num = ['9','15','17','35','53'] #atomic number of elements not found in proteins
    all_at_num = ['6','7','8','9','15','16','17','35','53'] #atomic number of all atoms in consideration
    drop_column_list = [] #will store the names of columns that need to be dropped. The names are in the format 'n.m' where n the at no. the protein 
    for  i in drop_protein_num:
        for j in all_at_num:
            drop_column_list.append(i+'.'+j)
    print("the number of columns being dropped is = ", len(drop_column_list)) 
    df_train1 = df_train.drop(columns = ['9.6', '9.7', '9.8', '9.9', '9.15', '9.16', '9.17', '9.35', '9.53', '15.6', '15.7', '15.8', '15.9', '15.15', '15.16', '15.17', '15.35', '15.53', '17.6', '17.7', '17.8', '17.9', '17.15', '17.16', '17.17', '17.35', '17.53', '35.6', '35.7', '35.8', '35.9', '35.15', '35.16', '35.17', '35.35', '35.53', '53.6', '53.7', '53.8', '53.9', '53.15', '53.16', '53.17', '53.35', '53.53'])
    print("Dimension of the training set after reducing dimensions= ", df_train1.shape)
    y_train = df_train1.values[:, 0] #stores the first column, which are the BA
    X_train = df_train1.values[:, 1:37] #stores the occurence counts of all complexes
    print("The dimensions of X_train np array: ", X_train.shape)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_minxmax = min_max_scaler.fit_transform(X_train) #scaling the data to range 0-1
    print("Scaled X_train ", X_train_minxmax[-3:-1])
    return [X_train_minxmax, y_train]
    
def process_carbonic_anhydrase():
    FILENAME1 = '/home/ira/Desktop/Minor Project/Featuresets/Refined_minus_carbonic_anhydrase.csv' #add the full path length of csv file of feature set of training data
    FILENAME2 = '/home/ira/Desktop/Minor Project/Featuresets/carbonic_anhydrase.csv' #tadd the full path length of the csv file of the feature set of the testing data
    op = prep_process(FILENAME1, FILENAME2)
    return op

def process_HIV_protease():
    FILENAME1 = '/home/ira/Desktop/Minor Project/Featuresets/Refined_minus_HIV_protease.csv' #add the full path length of csv file of feature set of training data
    FILENAME2 = '/home/ira/Desktop/Minor Project/Featuresets/HIV_protease.csv' #tadd the full path length of the csv file of the feature set of the testing data
    op = prep_process(FILENAME1, FILENAME2)
    return op
    
def process_trypsin():
    FILENAME1 = '/home/ira/Desktop/Minor Project/Featuresets/Refined_minus_trypsin.csv' #add the full path length of csv file of feature set of training data
    FILENAME2 = '/home/ira/Desktop/Minor Project/Featuresets/trypsin_index.csv' #tadd the full path length of the csv file of the feature set of the testing data
    op = prep_process(FILENAME1, FILENAME2)
    return op   
