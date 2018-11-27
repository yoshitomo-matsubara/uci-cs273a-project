# Basic Support for Diabetes 130-US hospitals for years 1999-2008 Data Set
https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008

## Requirements
- Python 3.6 >=
- Numpy
- Pandas

## data_loader
`import data_loader` or `from . import data_loader`
Note: import statement depends on your source root

### data_loader.***load_dataset***(*file_path*, *valid_rate*=0.1)
**Input**
- ***file_path***: label file path e.g. 'dataset_diabetes/diabetic_data.csv'
- ***valid_rate***: validation data rate (0 - 1), 0.1 by default

**Output**
- ***train_features***: training feature 2D-array (numpy.ndarray, str and int columns)
- ***train_labels***: training label array (numpy.ndarray)
- ***valid_features***: validation feature 2D-array (numpy.ndarray, str and int columns)
- ***valid_labels***: validation label array (numpy.ndarray)
- ***test_features***: test feature 2D-array (numpy.ndarray, str and int columns)
- ***test_labels***: test label array (numpy.ndarray)
- ***label_dict***: label dictionary (key: str, value: int)
