import os
import random

import numpy as np


def __get_file_path_list(dir_path, is_recursive=False, is_sorted=False):
    file_list = list()
    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)
        if os.path.isfile(path):
            file_list.append(path)
        elif is_recursive:
            file_list.extend(__get_file_path_list(path, is_recursive))
    return sorted(file_list) if is_sorted else file_list


def __load_texts(file_paths):
    text_list = list()
    for file_path in file_paths:
        with open(file_path, 'r') as fp:
            text = ' '.join([line.strip() for line in fp.readlines()])
        text_list.append(text)
    return text_list


def load_train_data(train_dir_path, valid_rate=0.1):
    pos_file_paths = __get_file_path_list(os.path.join(train_dir_path, 'pos/'))
    neg_file_paths = __get_file_path_list(os.path.join(train_dir_path, 'neg/'))
    pos_texts = __load_texts(pos_file_paths)
    neg_texts = __load_texts(neg_file_paths)
    train_text_list = list()
    train_label_list = list()
    valid_text_list = list()
    valid_label_list = list()
    np.random.seed(11)
    pos_mask = np.random.rand(len(pos_file_paths)) < 1 - valid_rate
    neg_mask = np.random.rand(len(neg_file_paths)) < 1 - valid_rate
    for pos_text, is_train in zip(pos_texts, pos_mask):
        if is_train:
            train_text_list.append(pos_text)
            train_label_list.append(1)
        else:
            valid_text_list.append(pos_text)
            valid_label_list.append(1)

    for neg_text, is_train in zip(neg_texts, neg_mask):
        if is_train:
            train_text_list.append(neg_text)
            train_label_list.append(0)
        else:
            valid_text_list.append(neg_text)
            valid_label_list.append(0)

    zipped_train_list = list(zip(train_text_list, train_label_list))
    random.shuffle(zipped_train_list)
    train_texts, train_labels = zip(*zipped_train_list)
    zipped_valid_list = list(zip(valid_text_list, valid_label_list))
    random.shuffle(zipped_valid_list)
    valid_texts, valid_labels = zip(*zipped_valid_list)
    return list(train_texts), np.array(list(train_labels)), list(valid_texts), np.array(list(valid_labels))


def load_test_data(test_dir_path):
    pos_file_paths = __get_file_path_list(os.path.join(test_dir_path, 'pos/'))
    neg_file_paths = __get_file_path_list(os.path.join(test_dir_path, 'neg/'))
    pos_texts = __load_texts(pos_file_paths)
    neg_texts = __load_texts(neg_file_paths)
    test_text_list = list()
    test_text_list.extend(pos_texts)
    test_text_list.extend(neg_texts)
    test_labels = np.hstack([np.ones(len(pos_texts), dtype=np.int), np.zeros(len(neg_texts), dtype=np.int)])
    zipped_test_list = list(zip(test_text_list, list(test_labels)))
    random.shuffle(zipped_test_list)
    test_texts, test_labels = zip(*zipped_test_list)
    return list(test_texts), np.array(list(test_labels))


def load_vocab_dict(vocab_file_path):
    vocab_dict = dict()
    with open(vocab_file_path, 'r') as fp:
        for line in fp:
            vocab_dict[line.strip()] = len(vocab_dict.keys())
    return vocab_dict
