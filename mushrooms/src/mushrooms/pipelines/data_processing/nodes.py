import pandas as pd



def preprocess_mushrooms(mushrooms: pd.DataFrame) -> pd.DataFrame:
    return mushrooms

def create_model_input_table(
    mushrooms: pd.DataFrame
) -> pd.DataFrame:

    model_input_table = mushrooms
    model_input_table = model_input_table.dropna()
    return model_input_table
