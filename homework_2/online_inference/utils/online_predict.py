import pandas as pd

from typing import List

from ml_project.run_pipeline import run_test_pipeline


def get_predict(params, features_dict: dict) -> List[int]:
    data_to_predict = pd.DataFrame(features_dict, index=[0])
    predict = run_test_pipeline(params, data_to_predict)
    list_predicts = predict.tolist()

    return list_predicts


# data = {
#     "age": 43,
#     "sex": 0,
#     "cp": 1,
#     "trestbps": 128,
#     "chol": 205,
#     "fbs": 1,
#     "restecg": 1,
#     "thalach": 184,
#     "exang": 0,
#     "oldpeak": 0,
#     "slope": 2,
#     "ca": 0,
#     "thal": 2
# }
#
# print(get_predict(1, data))
