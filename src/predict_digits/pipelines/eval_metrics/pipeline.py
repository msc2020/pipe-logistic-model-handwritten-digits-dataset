"""
This is a boilerplate pipeline 'pred_model'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import eval_model, plot_some_results


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        nodes=[
            Node(
                func=eval_model,
                inputs=['y_train', 'y_pred_train'],
                outputs='performance_metrics_train',
                name='eval_model_train_node',
            ),
            Node(
                func=eval_model,
                inputs=['y_test', 'y_pred_test'],
                outputs='performance_metrics_test',
                name='eval_model_test_node',
            ),
            Node(
                func=plot_some_results,
                inputs=['x_test', 'y_test', 'y_pred_test'],
                outputs='some_results_with_images',
                name='plot_some_results_node',
            )
        ]
    )
