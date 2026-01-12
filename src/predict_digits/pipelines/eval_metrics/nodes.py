import random

import pandas as pd
import numpy as np

from sklearn.metrics import classification_report

import matplotlib.pyplot as plt

# parameters for graphic configurations
SMALL_SIZE = 18

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize


def eval_model(
    y: np.ndarray,
    y_pred: np.ndarray,
) -> str:
    ''' Generate a classification report.

    Args:
        y: Values of target.
        y_pred: Values of the predicted values.

    Returns:
        A txt with the classification report for classification task.
    '''

    res = str(classification_report(y, y_pred, zero_division=np.nan))

    return res


def plot_some_results(
    x_test: np.ndarray,
    y_test: np.ndarray,
    y_pred_test: np.ndarray
) -> plt:
    ''' Plot some results with the respective images.
    '''

    # plot one random result
    # n_random = 42  # random.randint(0, len(y_pred_test))
    # img = x_test[n_random]
    # fig = plt.figure(figsize=(13, 5), dpi=40)
    # plt.imshow(img.reshape(8, 8), cmap='binary')
    # plt.axis('off')
    # plt.title(f'Prediction: {y_pred_test[n_random]}  (expected: {y_test[n_random]})')

    # plot 5 predicted digits with the respectives targets
    n_cols = 5
    _, axes = plt.subplots(nrows=1, ncols=n_cols, figsize=(25, 4), dpi=30)
    n_random = random.randint(0, len(y_pred_test))
    for ax, img, pred, target_y in zip(
        axes,
        x_test[n_random:n_random+n_cols],
        y_pred_test[n_random:n_random+n_cols],
        y_test[n_random:n_random+n_cols]
    ):
        ax.imshow(img.reshape(8, 8), cmap='binary')
        ax.set_title(f'Prediction: {pred}  (expected: {target_y})')
        ax.set_axis_off()

    plt.tight_layout()
    # plt.show()

    return plt
