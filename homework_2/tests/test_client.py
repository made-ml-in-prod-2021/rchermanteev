from fastapi.testclient import TestClient

from online_inference import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Homework 2"}


def test_predict_correct(correct_features):
    response = client.post("/predict", json=correct_features)
    assert response.status_code == 200


def test_predict_bad(bad_features):
    response = client.post("/predict", json=bad_features)
    assert response.status_code == 400
