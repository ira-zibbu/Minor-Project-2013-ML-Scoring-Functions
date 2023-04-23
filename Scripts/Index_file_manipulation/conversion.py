#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:51:16 2023
@author: ira
This file extracts the PDB IDs and the BA from the file PDBbind_2016_refinedset_v1.txt and writes it to another file PDBbind_2016_refinedset_v2.txt
"""
import os
lines = [] #will store the lines of the PDBbind_2016_refinedset_v1.txt file
op = [] #will store the lines to be written to the target file PDBbind_2016_refinedset_v2.txt
with open("/home/ira/Desktop/Minor Project/Index_files/PDBbind_2016_refinedset_v1.txt","r") as file1:
	for i in range(4056): #loops over all lines of PDBbind_2016_refinedset_v1.txt.
		lines.append(file1.readline()) #adding each line of the file as an element of the list
for i in lines: 
    temp = i.split(',') 
    string1 = temp[1] + '\t' + temp[2] + '\n'
    op.append(string1)
print("Task complete")
print("Size of refined set is ", len(op))
os.chdir("/home/ira/Desktop/Minor Project/Index_files")
file = open('PDBbind_2016_refinedset_v2.txt','w')
file.writelines(op)
file.close()
