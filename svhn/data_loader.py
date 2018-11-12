import numpy as np
import scipy.io


def load_train_data(train_file_path, axes=(3, 2, 0, 1), valid_rate=0.1):
    train_dict = scipy.io.loadmat(train_file_path)
    matrices = np.transpose(train_dict['X'], axes)
    labels = train_dict['y']
    np.random.seed(11)
    mask = np.random.rand(len(labels)) < 1 - valid_rate
    return matrices[mask], labels[mask], matrices[~mask], labels[~mask]


def load_test_data(test_file_path, axes=(3, 2, 0, 1)):
    test_dict = scipy.io.loadmat(test_file_path)
    return np.transpose(test_dict['X'], axes), test_dict['y']
