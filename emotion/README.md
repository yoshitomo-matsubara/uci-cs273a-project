# Basic Support for Facial Emotion Dataset
https://github.com/muxspace/facial_expressions

## Requirements
- Python 3.6 >=
- Numpy
- Pandas

## data_loader
`import data_loader` or `from . import data_loader`
Note: import statement depends on your source root

### data_loader.***load_dataset***(*img_dir_path*, *label_file_path*, *valid_rate*)
**Input**
- ***img_dir_path***: directory path of 'images/'
- ***label_file_path***: label file path e.g. 'data/legend.csv'
- ***valid_rate***: validation data rate (0 - 1), 0.1 by default

**Output**
- ***train_file_paths***: training image file path list
- ***train_labels***: training label array (numpy.ndarray)
- ***valid_file_paths***: validation image file path list
- ***valid_labels***: validation label array (numpy.ndarray)
- ***test_file_paths***: test image file path list
- ***test_labels***: test label array (numpy.ndarray)
- ***label_dict***: label dictionary (key: str, value: int)
