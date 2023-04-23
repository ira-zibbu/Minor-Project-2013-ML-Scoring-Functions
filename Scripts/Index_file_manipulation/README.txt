This directory contains python scripts used to generate or manipulate index files. Index files are needed to generate feature vectors. 

carbonic_anhydrase_index_generate.py: obtains the PDB IDs and BA of all carbonic anhydrase complexes from PDBbind 2016 refined set and prints them to a new index file
conversion.py: extracts the PDB IDs and the BA from the file PDBbind_2016_refinedset_v1.txt and writes it to another file PDBbind_2016_refinedset_v2.txt
crosscheck: verifies that two index files are disjoint and do not have any complexes in common
get_HIV_protease_index.py: obtains the PDB IDs and BA of all HIV-1 protease complexes from PDBbind 2016 refined set and prints them to an index file. 
subsetting.py: creates a new index file by removing complexes of one index file that are present in another indexfile
trypsin_index_generate.py: obtains the PDB IDs and BA of all typsin complexes from PDBbind 2016 refined set and prints them to an index file. 
