import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.model_selection import train_test_split
import wandb

def split_data(data: pd.DataFrame) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data.drop(columns=['class_e',"class_p"])
    y = data['class_e']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, shuffle=True
    )

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> [LogisticRegression, RandomForestClassifier]:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)

    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)
    return regressor, rfc


def evaluate_model(
    regressor: LogisticRegression, random_forest: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred_reg = regressor.predict(X_test)
    score_reg = r2_score(y_test, y_pred_reg)
    mse_reg = mean_squared_error(y_test, y_pred_reg)
    eva_reg = explained_variance_score(y_test, y_pred_reg)

    y_pred_rfc = random_forest.predict(X_test)
    score_rfc = r2_score(y_test, y_pred_rfc)
    mse_rfc = mean_squared_error(y_test, y_pred_rfc)
    eva_rfc = explained_variance_score(y_test, y_pred_rfc)

    logger = logging.getLogger(__name__)
    wandb.init(
        project="mushrooms"
    )
    wandb.log({
        "reg_r2":score_reg,
        "reg_mse":mse_reg,
        "reg_explained_variance":eva_reg,
        "score_rfc": score_rfc,
        "mse_rfc": mse_rfc,
        "eva_rfc":eva_rfc


    })

    wandb.finish()
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score_reg)
