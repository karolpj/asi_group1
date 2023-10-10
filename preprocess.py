import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess(df):
    df = df.apply(lambda x: pd.factorize(x)[0])
    if df.duplicated().sum() > 0:
        df.rop_duplicates
    X = df.drop(columns='class')
    y = df['class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=True)
    return X_train, X_test, y_train, y_test