import numpy as np
import pandas as pd


POS_STR = ' >50K'


def load_train_data(train_file_path, valid_rate=0.1, is_df=True):
    data_frame = pd.read_csv(train_file_path, header=None).sample(frac=1, random_state=11)
    np.random.seed(11)
    mask = np.random.rand(len(data_frame)) < 1 - valid_rate
    train_df, valid_df = data_frame.iloc[mask, :], data_frame.iloc[~mask, :]
    if is_df:
        return train_df, valid_df

    train_labels = [1 if x == POS_STR else 0 for x in train_df.iloc[:, 14].values]
    valid_labels = [1 if x == POS_STR else 0 for x in valid_df.iloc[:, 14].values]
    return train_df.iloc[:, :14].values, np.array(train_labels), valid_df.iloc[:, :14].values, np.array(valid_labels)


def load_test_data(test_file_path, is_df=True):
    data_frame = pd.read_csv(test_file_path, header=None, skiprows=1)
    if is_df:
        return data_frame

    test_labels = [1 if x == POS_STR else 0 for x in data_frame.iloc[:, 14].values]
    return data_frame.iloc[:, :14].values, np.array(test_labels)
