# Basic Support for The Street View House Numbers Dataset
http://ufldl.stanford.edu/housenumbers/

## Requirements
- Python 3.6 >=
- Numpy
- Scipy

## data_loader
`import data_loader` or `from . import data_loader`
Note: import statement depends on your source root

### data_loader.***load_train_data***(*train_file_path*, *axes*, *valid_rate*)
**Input**
- ***train_file_path***: training file path of 'train_32x32.mat'
- ***axes***: numpy matrix axes, (3, 2, 0, 1) by default
- ***valid_rate***: validation data rate (0 - 1), 0.1 by default

**Output**
- ***train_matrices***: training 4D-array (numpy.ndarray)
- ***train_labels***: training label array (numpy.ndarray)
- ***valid_matrices***: validation 4D-array (numpy.ndarray)
- ***valid_labels***: validation label array (numpy.ndarray)

---
### data_loader.***load_test_data***(*test_file_path*, *axes*)
**Input**
- ***test_file_path***: test file path of 'test_32x32.mat'
- ***axes***: numpy matrix axes, (3, 2, 0, 1) by default

**Output**
- ***test_matrices***: test 4D-array (numpy.ndarray)
- ***test_labels***: test label array (numpy.ndarray)
