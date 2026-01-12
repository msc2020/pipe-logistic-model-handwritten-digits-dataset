from kedro.pipeline import Node, Pipeline

from .nodes import split_dataset, normalize_dataset


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        nodes=[
            Node(
                func=split_dataset,
                inputs=['digits', 'target', 'params:split_options'],
                outputs=['x_train', 'x_test', 'y_train', 'y_test'],
                name='split_data_node',
            ),
            Node(
                func=normalize_dataset,
                inputs=['x_train'],
                outputs=['x_train_scaled', 'scaler'],
                name='normalize_data_node',
            ),
        ],
        namespace='data_processing_and_apply_model',
        prefix_datasets_with_namespace=False,  # obs: default = True
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
