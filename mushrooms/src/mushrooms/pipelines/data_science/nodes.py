import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
import wandb
from autogluon.tabular import TabularDataset, TabularPredictor


def split_data(data: pd.DataFrame) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    data.dropna(inplace=True)
    X = data.drop(columns=['class_e',"class_p"])
    y = data['class_e']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, shuffle=True
    )

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.DataFrame) -> TabularPredictor:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    label = "label"
    y_train = pd.DataFrame({"label":y_train})
    data = pd.concat([X_train,y_train],axis=1)
    train_data = TabularDataset(data)
    predictor = TabularPredictor(label=label).fit(train_data)
    return predictor


def evaluate_model(
    predictor: TabularPredictor, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_test = pd.DataFrame({"label":y_test})
    data = TabularDataset(pd.concat([X_test,y_test],axis=1))
    
    predictor.evaluate(data)

    predictor.leaderboard(data)

    logger = logging.getLogger(__name__)
    wandb.init(
        project="mushrooms"
    )
    
    #wandb.log({
    #    "reg_r2":score_reg,
    #    "reg_mse":mse_reg,
    #    "reg_explained_variance":eva_reg,
    #    "score_rfc": score_rfc,
    #    "mse_rfc": mse_rfc,
    #    "eva_rfc":eva_rfc

    wandb.finish()
    # logger.info("Model has a coefficient R^2 of %.3f on test data.", score_reg)
