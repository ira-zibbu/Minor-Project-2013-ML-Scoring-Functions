#this file cross-checks that no complexes from the one .txt file are present in another .txt  file

coreset = [] #a list that will store each line as strings in a list
refinedset = [] #a list that will store each line as strings in a list
duplicate = [] #list to store PDB IDs of any complexes that are duplicated between the set
with open("/home/ira/Desktop/Minor Project/Index_files/CASF_coreset2016.txt","r") as file1:
	for i in range(209): #loops over all lines of PDBbind_core07.txt
		coreset.append(file1.readline()) #adding each element of coreset
with open("/home/ira/Desktop/Minor Project/Index_files/PDBbind_trainingset_2016_index.txt","r") as file2:
	for i in range(3847): #loops over all lines of PDBbind_refined07-core07.txt
		refinedset.append(file2.readline()) #adding each element of refinedset
print(coreset[-3:-1]) #verifying that the entries are being read correctly
print(refinedset[-3:-1]) #verifying that the entries are being read correctly
for i in range(len(coreset)): #loops over all entries of the coreset
	for j in range(len(refinedset)): #loops over all entries of the refineset
		core_temp = coreset[i] #store the ith string of the core set
		refined_temp = refinedset[j] #store the jth string of refined set
		#print("core_temp", core_temp)
		#print("refined_temp", refined_temp)
		core_PDBID = [] #will store the characters of the PDB ID of the ith entry of the core set
		refined_PDBID = [] # #will store the characters of the PDB ID of the jth entry of refined set
		for k in range(4): #loops over the first 4 characters of the ith and jth strings of the coreset and refined set respectively to get the PDB IDs
			core_PDBID.append(core_temp[k]) 
			refined_PDBID.append(refined_temp[k])
		#print("core_PDBID is ", core_PDBID)
		#print("refined_PDBID is ", refined_PDBID)
		flag = True #flag is True if core_PDBID is same as refined_PDBID 
		for m in range(4):
			if core_PDBID[m] != refined_PDBID[m]:
				flag = False #becomes false if two corresponding characters are unequal
		if flag == True:
			duplicate.append(coreset[i])
print("These are the complexes are they are duplicated: ", duplicate)
		
		
		
			
