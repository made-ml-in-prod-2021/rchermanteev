from typing import Union

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


SklearnRegressionModel = Union[RandomForestClassifier, LogisticRegression]


def predict_model(model: SklearnRegressionModel, features: pd.DataFrame) -> np.ndarray:
    predicts = model.predict(features)

    return predicts
