This folder contains all python scripts for the general test and the protein specific tests. For more information, refer to the report PDF or the individual scripts. The MODELS scripts need to be present in the same directory as processdata.py

MODELS: Hyperparamters for these models were optimized on the primary training set.
The training and test sets being used by this modules can be changed by calling different functions from processdata.py

kNN.py: This module uses the k nearest neighbours algorithm for regression to predict binding affinities for the training dataset
lin_regress.py: This module uses linear regression to predict binding affinities for the training dataset
MARS.py: This module uses MARS to predict binding affinities for the training dataset
Random_Forest.py: This module uses random forest to predict binding affinities for the training dataset
Support_vector_regress.py: This module uses SVM regression to predict binding affinities for the training set.
novel_protein_tests: trains and tests models on the novel protein specific tests.

processdata.py: loads the .csv feature sets, drops the zero-value features, normalizes the data
