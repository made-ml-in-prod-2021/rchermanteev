import pytest

correct_features = [
    {
        "age": 52,
        "sex": 1,
        "cp": 1,
        "trestbps": 128,
        "chol": 205,
        "fbs": 1,
        "restecg": 1,
        "thalach": 184,
        "exang": 0,
        "oldpeak": 0,
        "slope": 2,
        "ca": 0,
        "thal": 2,
    },
    {
        "age": 43,
        "sex": 0,
        "cp": 1,
        "trestbps": 128,
        "chol": 205,
        "fbs": 1,
        "restecg": 1,
        "thalach": 184,
        "exang": 0,
        "oldpeak": 0,
        "slope": 2,
        "ca": 0,
        "thal": 2,
    },
]

bad_features = [
    {
        "age": 140,
        "sex": 1,
        "cp": 1,
        "trestbps": 128,
        "chol": 205,
        "fbs": 1,
        "restecg": 1,
        "thalach": 184,
        "exang": 0,
        "oldpeak": 0,
        "slope": 2,
        "ca": 0,
        "thal": 2,
    },
    {
        "age": 43,
        "sex": 4,
        "cp": 1,
        "trestbps": 128,
        "chol": 205,
        "fbs": 1,
        "restecg": 1,
        "thalach": 184,
        "exang": 0,
        "oldpeak": 0,
        "slope": 2,
        "ca": 0,
        "thal": 2,
    },
]


@pytest.fixture(params=correct_features)
def correct_features(request):
    return request.param


@pytest.fixture(params=bad_features)
def bad_features(request):
    return request.param
