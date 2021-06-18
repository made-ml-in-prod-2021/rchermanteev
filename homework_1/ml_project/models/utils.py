import pickle
import joblib

from cloudpickle import dump
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, roc_auc_score

SklearnRegressionModel = Union[RandomForestClassifier, LogisticRegression]


def evaluate_model(predicts: np.ndarray, target: pd.Series, metrics_list) -> Dict[str, float]:

    cm = confusion_matrix(target, predicts)
    sensitivity = cm[0, 0] / (cm[0, 0] + cm[1, 0])
    specificity = cm[1, 1] / (cm[1, 1] + cm[0, 1])

    metrics = {}
    if "accuracy_score" in metrics_list:
        metrics["accuracy_score"] = accuracy_score(target, predicts)

    if "cm_sensitivity" in metrics_list:
        metrics["cm_sensitivity"] = sensitivity

    if "cm_specificity" in metrics_list:
        metrics["cm_specificity"] = specificity

    if "f1_score" in metrics_list:
        metrics["f1_score"] = f1_score(target, predicts)

    if "roc_auc_score" in metrics_list:
        metrics["roc_auc_score"] = roc_auc_score(target, predicts)

    return metrics


def serialize_model(model: object, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output


def serialize_transformer_params(transform: object, output: str) -> str:
    with open(output, "wb") as f:
        dump(transform, f)
    return output


def get_model_to_predict(filepath_to_model: str) -> SklearnRegressionModel:
    model = joblib.load(filepath_to_model)
    return model
