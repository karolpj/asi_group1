from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_mushrooms


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_mushrooms,
                inputs="mushrooms",
                outputs="preprocessed_mushrooms",
                name="preprocess_mushrooms_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_mushrooms"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )
