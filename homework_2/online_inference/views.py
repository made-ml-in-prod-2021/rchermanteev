import os
import json

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from online_inference import app
from .utils import get_predict
from .templates import FeaturesToPredict
from ml_project.enities.train_pipeline_params import (
    read_run_params,
)
from ml_project.run_pipeline import run_train_pipeline


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.get("/")
def root():
    return {"message": "Homework 2"}


@app.post("/predict")
def read_item(features: FeaturesToPredict):
    # TODO: Добавить выбор другой модели
    params = read_run_params("configs/run_config_random_forest.yml")
    if not (
        os.path.exists(params.output_model_path)
        and os.path.exists(params.transformer_params_path)
    ):
        run_train_pipeline(params)

    features_dict = features.dict()
    predict = get_predict(params, features_dict)

    return {"data": features_dict, "predicts": predict}
