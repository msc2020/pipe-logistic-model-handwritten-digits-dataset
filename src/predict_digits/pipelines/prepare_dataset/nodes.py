import pandas as pd
import numpy as np
import logging

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def split_dataset(x: pd.DataFrame, y: pd.DataFrame, parameters: dict) -> list:
    '''Splits data into features and targets training and test sets.

    Args:
        x: Data containing features.
        y: Data of the target.
        parameters: Parameters defined in conf/base/parameters_prepare_dataset.yml.
    Returns:
        Inputs data x and y are splited and returned as x_train, x_test, y_train, y_test.
    '''
    x_train, x_test, y_train, y_test = train_test_split(
        x, y,
        test_size=parameters['test_size'],
        random_state=parameters['random_state']
    )
    logger = logging.getLogger(__name__)
    msg = f'''
    Dataset split:
      - x: {x.shape} -> x_train: {x_train.shape}, x_test: {x_test.shape}
      - y: {y.shape} -> y_train: {y_train.shape}, y_test: {y_test.shape}'''
    logger.info(msg)
    return x_train.values, x_test.values, y_train.values.ravel(), y_test.values.ravel()


def normalize_dataset(x_train: np.ndarray) -> StandardScaler:
    ''' Normalize dataset.
    '''
    scaler = StandardScaler().fit(x_train)
    x_train_scaled = scaler.transform(x_train)

    return x_train_scaled, scaler
