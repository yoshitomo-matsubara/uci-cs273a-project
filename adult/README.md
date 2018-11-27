# Basic Support for Adult Dataset
https://archive.ics.uci.edu/ml/datasets/adult

## Requirements
- Python 3.6 >=
- Numpy
- Pandas

## data_loader
`import data_loader` or `from . import data_loader`
Note: import statement depends on your source root

### data_loader.***load_train_data***(*train_file_path*, *valid_rate*=0.1, *is_df*=True)
**Input**
- ***train_file_path***: training file path of 'adult.data'
- ***valid_rate***: validation data rate (0 - 1), 0.1 by default
- ***is_df***: whether or not returned objects are pandas.DataFrame, True by default

**Output**
- ***train_features***: training feature 2D-array (numpy.ndarray, str and int columns)
- ***train_labels***: training label array (numpy.ndarray)
- ***valid_features***: validation feature 2D-array (numpy.ndarray, str and int columns)
- ***valid_labels***: validation label array (numpy.ndarray)

---
### data_loader.***load_test_data***(*test_file_path*, *is_df*=True)
**Input**
- ***test_file_path***: test file path of 'adult.test'
- ***is_df***: whether or not returned objects are pandas.DataFrame, True by default

**Output**
- ***test_features***: test feature 2D-array (numpy.ndarray, str and int columns)
- ***test_labels***: test label array (numpy.ndarray)
