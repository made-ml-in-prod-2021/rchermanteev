import pandas as pd

from typing import List

from ml_project.run_pipeline import run_test_pipeline


def get_predict(params, features_dict: dict) -> List[int]:
    data_to_predict = pd.DataFrame(features_dict, index=[0])
    predict = run_test_pipeline(params, data_to_predict)
    list_predicts = predict.tolist()

    return list_predicts
