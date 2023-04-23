
#9 March 2023
def subset_index_files(FILENAME1, size_file1, FILENAME2, size_file2, FILEOUT_NAME):
    import os
    coreset = [] #a list that will store each line as strings in a list
    refinedset = [] #a list that will store each line as strings in a list
    trainingset = [] #list to store the training sets
    with open(FILENAME1,"r") as file1:
    	for i in range(size_file1): #loops over all lines of CASF_coreset2016.txt
    		coreset.append(file1.readline()) #adding each element of coreset
    with open(FILENAME2,"r") as file2:
    	for i in range(size_file2): #loops over all lines of PDBbind_refinedset2016.txt
    		refinedset.append(file2.readline()) #adding each element of refinedset
    print(coreset[-3:-1]) #verifying that the entries are being read correctly
    print(refinedset[-3:-1]) #verifying that the entries are being read correctly
    for i in refinedset:
        flag1 = False
        for j in coreset:
            refined_PDBID = i[0:4]
            coreset_PDBID = j[0:4]
            if coreset_PDBID == refined_PDBID:
                flag1 = True
                break
        if flag1 == False:
            trainingset.append(i)
    print("task complete")
    print("Size of training set is ", len(trainingset))
    print(trainingset[0:10])
    os.chdir("/home/ira/Desktop/Minor Project/Index_files")
    file = open(FILEOUT_NAME,'w')
    file.writelines(trainingset)
    file.close()		
    

            


