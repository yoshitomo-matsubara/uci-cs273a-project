import random

import numpy as np
import pandas as pd


def __append_data(data, features_list, label_list, label_dict):
    for sample in data:
        features_list.append(sample[:-1])
        label_list.append(label_dict[sample[-1].lower()])


def load_dataset(file_path, valid_rate=0.1):
    data_frame = pd.read_csv(file_path).sample(frac=1, random_state=11)
    label_dict = dict()
    for label_name in set([key.lower() for key in data_frame.iloc[:, -1].unique()]):
        label_dict[label_name] = len(label_dict.keys())

    label_data_dict = dict()
    for sample in data_frame.values:
        label = sample[-1]
        if label not in label_data_dict:
            label_data_dict[label] = list()
        label_data_dict[label].append(sample)

    train_features_list = list()
    train_label_list = list()
    valid_features_list = list()
    valid_label_list = list()
    test_features_list = list()
    test_label_list = list()
    for label in label_data_dict.keys():
        data = label_data_dict[label]
        test_size = int(len(data) * 0.1)
        train_data = data[:-test_size]
        valid_size = int(len(train_data) * valid_rate)
        __append_data(train_data[:-valid_size], train_features_list, train_label_list, label_dict)
        __append_data(train_data[-valid_size:], valid_features_list, valid_label_list, label_dict)
        __append_data(data[-test_size:], test_features_list, test_label_list, label_dict)

    zipped_train_list = list(zip(train_features_list, train_label_list))
    random.shuffle(zipped_train_list)
    test_features, train_labels = zip(*zipped_train_list)
    return np.stack(list(test_features)), np.array(list(train_labels)), np.stack(valid_features_list),\
           np.array(valid_label_list), np.stack(test_features_list), np.array(test_label_list), label_dict
