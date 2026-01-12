import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def apply_model(
    x_input: np.ndarray,
    model_clf: LogisticRegression,
    scaler: StandardScaler,
) -> np.ndarray:
    '''Trains the models for classification tasks.

    Args:
        x_train: Training data of independent features.

    Returns:
        A model trained.
    '''
    x_scaled = scaler.transform(x_input)
    y_pred = model_clf.predict(x_scaled)

    return np.array(y_pred)
