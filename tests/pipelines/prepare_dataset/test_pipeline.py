"""
This is a boilerplate test file for pipeline 'prepare_dataset'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""


import logging
import numpy as np
import pytest
from kedro.io import DataCatalog, MemoryDataset
from kedro.runner import SequentialRunner
from predict_digits.pipelines.prepare_dataset import create_pipeline


@pytest.fixture
def dummy_x():
    x_dummy = np.array([
        [
            0.,  0.,  0.,  7., 12.,  0.,  0.,  0.,  0.,  0.,  4., 16.,  8.,
            0.,  0.,  0.,  0.,  0., 12., 11.,  0.,  0.,  0.,  0.,  0.,  0.,
            15., 10.,  8.,  6.,  1.,  0.,  0.,  0., 15., 16.,  8., 10.,  8.,
            0.,  0.,  0., 14.,  7.,  0.,  0., 12.,  0.,  0.,  0.,  8., 11.,
            0.,  5., 16.,  2.,  0.,  0.,  0.,  9., 14., 14.,  5.,  0.
        ],
        [
            0.,  0., 11., 16.,  8.,  0.,  0.,  0.,  0.,  6., 16., 11., 13.,
            9.,  0.,  0.,  0.,  7., 16.,  0.,  9., 16.,  0.,  0.,  0.,  2.,
            15., 12., 16., 16.,  3.,  0.,  0.,  0.,  5.,  7.,  7., 16.,  4.,
            0.,  0.,  0.,  0.,  0.,  5., 16.,  5.,  0.,  0.,  0.,  3.,  7.,
            16., 11.,  0.,  0.,  0.,  0., 13., 16., 11.,  1.,  0.,  0.
        ],
        [
            0.,  0.,  8., 15., 12.,  4.,  0.,  0.,  0.,  5., 14.,  4., 11.,
            7.,  0.,  0.,  0.,  0.,  0.,  1., 14.,  3.,  0.,  0.,  0.,  0.,
            2., 15., 14.,  1.,  0.,  0.,  0.,  0.,  0.,  8., 13., 11.,  0.,
            0.,  0.,  0.,  0.,  0.,  0., 13.,  5.,  0.,  0.,  0., 12.,  2.,
            3., 12.,  7.,  0.,  0.,  0., 13., 16., 15.,  8.,  0.,  0.
        ]
    ])
    return x_dummy


@pytest.fixture
def dummy_y():
    y_dummy = np.array([6, 9, 3])
    return y_dummy


@pytest.fixture
def dummy_parameters():
    parameters = {
        'split_options': {
            'test_size': 0.33,
            'random_state': 42
        }
    }
    return parameters


def test_prepare_dataset(caplog, dummy_x, dummy_y, dummy_parameters):
    pipeline = (
        create_pipeline()
        .from_nodes('data_processing_and_apply_model.split_data_node',)
        .to_nodes('data_processing_and_apply_model.normalize_data_node')
    )
    dummy_catalog = {
        'digits': MemoryDataset(data=dummy_x()),
        'target': MemoryDataset(data=dummy_y()),
        'params:split_options': MemoryDataset(data=dummy_parameters()),
    }
    catalog = DataCatalog()# + DataCatalog(datasets=dummy_catalog)
    # catalog = DataCatalog(datasets=dummy_catalog)
    # caplog.set_level(logging.DEBUG, logger='kedro')
    successful_run_msg = 'Pipeline execution completed successfully.'

    SequentialRunner().run(pipeline, catalog)

    assert successful_run_msg in caplog.text


# def test_prepare_dataset(caplog, dummy_x, dummy_y, dummy_parameters):
#     pipeline = (
#         create_pipeline()
#         .from_nodes('data_processing_and_apply_model.split_data_node',)
#         .to_nodes('data_processing_and_apply_model.normalize_data_node')
#     )
#     dummy_catalog = {
#         'x': MemoryDataset(data=dummy_x()),
#         'y': MemoryDataset(data=dummy_y()),
#         'parameters': MemoryDataset(data=dummy_parameters()),
#     }

#     catalog = DataCatalog(datasets=dummy_catalog)
#     caplog.set_level(logging.DEBUG, logger='kedro')
#     successful_run_msg = 'Pipeline execution completed successfully.'

#     SequentialRunner().run(pipeline, catalog)

#     assert successful_run_msg in caplog.text
