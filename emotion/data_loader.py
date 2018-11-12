import os
import random

import numpy as np
import pandas as pd


def __append_data(data, file_path_list, label_list, img_dir_path, label_dict):
    for sample in data:
        file_path_list.append(os.path.join(img_dir_path, sample[1]))
        label_list.append(label_dict[sample[2].lower()])


def load_dataset(img_dir_path, label_file_path, valid_rate=0.1):
    data_frame = pd.read_csv(label_file_path).sample(frac=1, random_state=11)
    label_dict = dict()
    for label_name in set([key.lower() for key in data_frame['emotion'].unique()]):
        label_dict[label_name] = len(label_dict.keys())

    label_data_dict = dict()
    for sample in data_frame.values:
        label = sample[2]
        if label not in label_data_dict:
            label_data_dict[label] = list()
        label_data_dict[label].append(sample)

    train_file_path_list = list()
    train_label_list = list()
    valid_file_path_list = list()
    valid_label_list = list()
    test_file_path_list = list()
    test_label_list = list()
    for label in label_data_dict.keys():
        data = label_data_dict[label]
        test_size = int(len(data) * 0.1)
        train_data = data[:-test_size]
        valid_size = int(len(train_data) * valid_rate)
        __append_data(train_data[:-valid_size], train_file_path_list, train_label_list, img_dir_path, label_dict)
        __append_data(train_data[-valid_size:], valid_file_path_list, valid_label_list, img_dir_path, label_dict)
        __append_data(data[-test_size:], test_file_path_list, test_label_list, img_dir_path, label_dict)

    zipped_train_list = list(zip(train_file_path_list, train_label_list))
    random.shuffle(zipped_train_list)
    train_file_paths, train_labels = zip(*zipped_train_list)
    return [*train_file_paths], np.array([*train_labels]), valid_file_path_list, np.array(valid_label_list),\
           test_file_path_list, np.array(test_label_list), label_dict
