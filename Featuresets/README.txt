Featuresets directory

This directory stores the extracted feature representations of the datasets indicated in Index_files
Each .csv file has the following structure:
- The first column is the binding affinity of that complex. 
- The next 81 columns are of the form n.m and representing the occurence count for the n-m atom pair. It is the number of interacting atoms of at wt n of the protein with atoms of at wt m of the ligand. Eg: 6.7 is the number of carbon atoms of protein - nitrogen atom of ligand pairs that interact (proximity is below the threshold 12A)
- The last column contains the PDB ID of the protein of the complex

These .csv files are the outputs of RF-Score.c (Ballester, Pedro J., and John B. O. Mitchell. “A Machine Learning Approach to Predicting Protein–Ligand Binding Affinity with Applications to Molecular Docking.” Bioinformatics, vol. 26, no. 9, May 2010. The c programs for RF-Score can be found on http://chemistry.st-andrews.ac.uk/staff/jbom/group/RF-Score.html. 

The csv files here correspond to index files in \Index_files. More information on these data sets can be found in the report PDF.

