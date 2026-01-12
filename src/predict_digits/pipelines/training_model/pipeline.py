from kedro.pipeline import Node, Pipeline

from .nodes import train_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            Node(
                func=train_model,
                inputs=['x_train_scaled', 'y_train', 'params:model_options'],
                outputs='model_clf',
                name='train_model_node',
            )
        ]
    )




## manual pipeline
# pipeline_prepare_dataset = pipeline(
#     [
#         Node(
#             func=split_data,
#             inputs=['digits', 'target', 'params:split_options'],
#             outputs=['X_train', 'X_test', 'y_train', 'y_test'],
#             name='split_data_node',
#         ),
#         Node(
#             func=normalize_data,
#             inputs=['X_train', 'X'],
#             outputs=['X_train_scaled', 'scaler'],
#             name='normalize_data_node',
#         )
#     ]
# )


# pipeline_prepare_dataset_input = pipeline(
#     pipeline_prepare_dataset,
#     namespace='preprocessing'
# )
