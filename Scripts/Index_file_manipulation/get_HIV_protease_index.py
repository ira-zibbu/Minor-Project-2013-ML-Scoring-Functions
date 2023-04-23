#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:21:13 2023
This file obtains the PDB IDs and BA of all HIV-1 protease complexes and prints them to an index file. 
It also creates the index file of the training set by removing all HIV-1 protease
@author: ira
"""
import os
from subsetting import  subset_index_files
lines_refinedset_names = [] #will store the lines of the INDEX_refined_name_2016.txt
lines_refinedset_ba = [] #will store the lines of PDBbind_2016_refinedset_v2.txt
lines_HIV = [] #
with open("/home/ira/Desktop/Minor Project/Index_files/PDBbind_2016_plain_text_index/index/INDEX_refined_name_2016.txt","r") as file2: 
	for i in range(4057): #loops over all lines of textfile
		lines_refinedset_names.append(file2.readline()) #
with open("/home/ira/Desktop/Minor Project/Index_files/PDBbind_2016_refinedset_v2.txt","r") as file2: 
	for i in range(4057): #loops over all lines of textfile
		lines_refinedset_ba.append(file2.readline()) #
for j in lines_refinedset_names: #looping over the lines_refinedset to find the name of the protein for the corresponding PDB_ID
    protein_name = ' '.join(j.split()[3:-1]) + " " + j.split()[-1]
    print("Protein name = ", protein_name)
    PDB_ID = " "
    if protein_name == "HIV-1 PROTEASE":
        PDB_ID = j.split()[0]
        for k in lines_refinedset_ba:
            k_ID = k[0:4]
            if PDB_ID == k_ID:
                lines_HIV.append(k)
os.chdir("/home/ira/Desktop/Minor Project/Index_files")
file = open('HIV_protease.txt','w')
file.writelines(lines_HIV)
file.close()
REFINED_SET_FILENAME = "/home/ira/Desktop/Minor Project/Index_files/PDBbind_2016_refinedset_v2.txt"
HIV_PROTEASE_FILENAME = "/home/ira/Desktop/Minor Project/Index_files/HIV_protease.txt"
subset_index_files(HIV_PROTEASE_FILENAME, 280, REFINED_SET_FILENAME, 4056, "Refined_minus_HIV_protease.txt")
    
    