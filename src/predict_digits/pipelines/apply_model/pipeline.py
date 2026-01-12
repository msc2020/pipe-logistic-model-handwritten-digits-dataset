"""
This is a boilerplate pipeline 'pred_model'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import apply_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        nodes=[
            Node(
                func=apply_model,
                inputs=['x_train', 'model_clf', 'scaler'],
                outputs='y_pred_train',
                name='apply_model_train_node',
            ),
            Node(
                func=apply_model,
                inputs=['x_test', 'model_clf', 'scaler'],
                outputs='y_pred_test',
                name='apply_model_test_node',
            )
        ]
    )
