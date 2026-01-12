import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression


def train_model(
    x_train: np.ndarray,
    y_train: np.ndarray,
    parameters: dict
) -> LogisticRegression:
    ''''Trains the linear regression model.

    Args:
        x_train: Training data of independent features.

    Returns:
        A model trained.'''

    model_clf = LogisticRegression()
    model_clf.fit(x_train, y_train.ravel(), parameters['random_state'])

    return model_clf
