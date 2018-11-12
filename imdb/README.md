# Basic Support for Large Movie Review Dataset
http://ai.stanford.edu/~amaas/data/sentiment/

## Requirements
- Python 3.6 >=
- Numpy

## data_loader
`import data_loader` or `from . import data_loader`
Note: import statement depends on your source root

### data_loader.***load_train_data***(*train_dir_path*, *valid_rate*=0.1)
**Input**
- ***train_dir_path***: training directory path e.g. './aclImdb/train/'
- ***valid_rate***: validation data rate (0 - 1), 0.1 by default

**Output**
- ***train_texts***: training text list
- ***train_labels***: training label array (numpy.ndarray, 0: negative, 1:positive)
- ***valid_texts***: validation text list
- ***valid_labels***: validation label array (numpy.ndarray, 0: negative, 1:positive)

---
### data_loader.***load_test_data***(*test_dir_path*)
**Input**
- ***test_dir_path***: test directory path e.g. './aclImdb/test/'

**Output**
- ***test_texts***: test text list
- ***test_labels***: test label array (numpy.ndarray, 0: negative, 1:positive)

---
### data_loader.***load_vocab_dict***(*vocab_file_path*)
**Input**
- ***vocab_file_path***: vocabulary file path e.g. './aclImdb/imdb.vocab'

**Output**
- ***vocab_dict***: vocabulary dictionary (key: str, value: int)
