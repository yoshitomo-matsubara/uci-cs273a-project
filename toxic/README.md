# Basic Support for Toxic Comment Challenge
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge

## Requirements
- Python 3.6 >=
- Numpy
- Pandas

## data_loader
`import data_loader` or `from . import data_loader`
Note: import statement depends on your source root

### data_loader.***load_train_data***(*train_file_path*, *valid_rate*, *is_df*)
**Input**
- ***train_file_path***: file path of 'train.csv'
- ***valid_rate***: validation data rate (0 - 1), 0.1 by default
- ***is_df***: whether or not returned objects are pandas.DataFrame, True by default

**Output** (***is_df***: True)
- ***train_df***: training data frame
- ***valid_df***: validation data frame

**Output** (***is_df***: False)
- ***train_ids***: training ID list
- ***train_texts***: training text list
- ***train_labels***: training label 2D-array (numpy.ndarray, 6 columns, 0: negative, 1:positive)
- ***valid_ids***: validation ID list
- ***valid_texts***: validation text list
- ***valid_labels***: validation label 2D-array (numpy.ndarray, 6 columns, 0: negative, 1:positive)

---
### data_loader.***load_test_data***(*test_file_path*, *test_label_file_path*, *is_df*)
**Input**
- ***train_file_path***: file path of 'test.csv'
- ***test_label_file_path***: file path of 'test_labels.csv'
- ***is_df***: whether or not returned objects are pandas.DataFrame, True by default


**Output** (***is_df***: True)
- ***test_df***: test data frame

**Output** (***is_df***: False)
- ***test_ids***: test ID list
- ***test_texts***: test text list
- ***test_labels***: test label 2D-array (numpy.ndarray, 6 columns, 0: negative, 1:positive)
