import numpy as np
import pandas as pd


def load_train_data(train_file_path, valid_rate=0.1, is_df=True):
    data_frame = pd.read_csv(train_file_path).sample(frac=1, random_state=11)
    np.random.seed(11)
    mask = np.random.rand(len(data_frame)) < 1 - valid_rate
    train_df, valid_df = data_frame.iloc[mask, :], data_frame.iloc[~mask, :]
    if is_df:
        return train_df, valid_df

    # train_ids, train_texts, train_labels (6 columns), valid_ids, valid_texts, valid_labels (6 columns)
    return train_df['id'].tolist(), train_df['comment_text'].tolist(), train_df.iloc[:, 2:].as_matrix(),\
           valid_df['id'].tolist(), valid_df['comment_text'].tolist(), valid_df.iloc[:, 2:].as_matrix()


def load_test_data(test_file_path, test_label_file_path, is_df=True):
    data_frame = pd.read_csv(test_file_path)
    label_frame = pd.read_csv(test_label_file_path)
    targets = label_frame['toxic'] != -1
    data_frame, label_frame = data_frame[targets], label_frame[targets]
    if is_df:
        return pd.concat([data_frame, label_frame.iloc[:, 1:]], 1)

    # test_ids, test_texts, test_labels (6 columns)
    return data_frame['id'].tolist(), data_frame['comment_text'].tolist(), data_frame.iloc[:, 1:].as_matrix()
