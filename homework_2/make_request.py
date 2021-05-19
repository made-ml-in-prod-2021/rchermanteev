import numpy as np
import requests

if __name__ == "__main__":
    for _ in range(10):
        request_data = {
            "age": np.random.randint(0, 130),
            "sex": np.random.randint(0, 2),
            "cp": np.random.randint(0, 1),
            "trestbps": np.random.randint(0, 128),
            "chol": np.random.randint(0, 205),
            "fbs": np.random.randint(0, 1),
            "restecg": np.random.randint(0, 1),
            "thalach": np.random.randint(0, 184),
            "exang": np.random.randint(0, 1),
            "oldpeak": np.random.randint(0, 1),
            "slope": np.random.randint(0, 3),
            "ca": np.random.randint(0, 3),
            "thal": np.random.randint(0, 3),
        }
        print(request_data)
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=request_data,
        )
        print(response.status_code)
        print(response.text)
