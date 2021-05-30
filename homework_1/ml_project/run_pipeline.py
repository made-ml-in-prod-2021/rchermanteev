import json

import click
import logging
import logging.config
import pandas as pd
import yaml

from cloudpickle import load

from data import read_data, split_train_val_data
from enities.train_pipeline_params import (
    read_train_params,
)
from enities.predict_pipeline_params import (
    read_test_params,
)
from features import make_features
from features.build_features import extract_target, build_transformer
from models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
    get_model_to_predict,
    serialize_transformer_params,
)

logger = logging.getLogger("ml_project")


def setup_logging(filepath):
    with open(filepath) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))


def run_test_pipeline(training_pipeline_params):
    logger.info("Start test pipeline")
    logger.info("Read data to test")
    data_to_predict = read_data(training_pipeline_params.test_data_path)
    logger.info("Shape test data - (%s)", data_to_predict.shape)
    with open(training_pipeline_params.transformer_params_path, "rb") as f:
        logger.info("Load transformer")
        transformer = load(f)

    logger.info("Load model")
    model = get_model_to_predict(training_pipeline_params.output_model_path)
    logger.info("Transform test data")
    transform_data = transformer.transform(data_to_predict)
    logger.info("Transformed test data shape - (%s)", transform_data.shape)
    logger.info("Get predicts")
    predicts = model.predict(transform_data)
    logger.info("Predicts shape - (%s)", predicts.shape)
    pd.DataFrame(predicts, columns=["target"]).to_csv(
        training_pipeline_params.predicts_path
    )
    logger.info("Predicts saved in file - (%s)", training_pipeline_params.predicts_path)


def run_train_pipeline(training_pipeline_params):
    logger.info("Start train pipeline")
    logger.info("Read data to train")
    data = read_data(training_pipeline_params.train_data_path)
    logger.info("Shape train data - (%s)", data.shape)
    logger.info(
        "Start split data to train with params - (%s)",
        training_pipeline_params.splitting_params,
    )
    train_df, val_df = split_train_val_data(
        data, training_pipeline_params.splitting_params
    )
    logger.info("Shape train_df data - (%s)", train_df.shape)
    logger.info("Shape val_df data - (%s)", val_df.shape)
    logger.info(
        "Target column in data - (%s)",
        training_pipeline_params.feature_params.target_col,
    )
    val_target = extract_target(val_df, training_pipeline_params.feature_params)
    logger.info("Extract target column with shape(%s) from val_df", val_target.shape)
    train_target = extract_target(train_df, training_pipeline_params.feature_params)
    logger.info("Extract target column with shape(%s) from val_df", train_target.shape)

    train_df = train_df.drop(training_pipeline_params.feature_params.target_col, 1)
    logger.info("Shape train_df data after drop target column - (%s)", train_df.shape)
    val_df = val_df.drop(training_pipeline_params.feature_params.target_col, 1)
    logger.info("Shape val_df data after drop target column - (%s)", train_df.shape)
    transformer = build_transformer(training_pipeline_params.feature_params)
    logger.info(
        "Build transformer with params - (%s)", training_pipeline_params.feature_params
    )
    transformer.fit(train_df)
    logger.info("Fit transformer on data with shape - (%s)", train_df.shape)
    train_features = make_features(transformer, train_df)
    logger.info("Created train features with shape - (%s)", train_features.shape)
    model = train_model(
        train_features, train_target, training_pipeline_params.train_params
    )
    logger.info(
        "Trained model with params - (%s)", training_pipeline_params.train_params
    )
    val_features = make_features(transformer, val_df)
    logger.info("Created val features with shape - (%s)", train_features.shape)
    logger.info("Get predicts")
    predicts = predict_model(model, val_features)
    logger.info("Predicts shape - (%s)", predicts.shape)
    metrics = evaluate_model(predicts, val_target, training_pipeline_params.train_params.metrics_list)
    logger.info("Evaluated model result - (%s)", metrics)
    with open(training_pipeline_params.metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
        logger.info(
            "Saved metrics in file - (%s)", training_pipeline_params.metric_path
        )

    path_to_model = serialize_model(model, training_pipeline_params.output_model_path)
    logger.info("Saved model in file - (%s)", path_to_model)

    path_to_transformer_params = serialize_transformer_params(
        transformer, training_pipeline_params.transformer_params_path
    )
    logger.info("Saved transformer_params in file - (%s)", path_to_transformer_params)


@click.command(name="run")
@click.argument("config_path")
@click.argument("train_or_predict")
def pipeline_command(config_path: str, train_or_predict: str):
    if train_or_predict == "train":
        params = read_train_params(config_path)
    elif train_or_predict == "predict":
        params = read_test_params(config_path)

    setup_logging(params.logging_config_path)
    logger.info("Start app in mode - (%s)", train_or_predict)
    logger.info("Read run params from - (%s)", config_path)
    logger.info("Read logging params from - (%s)", params.logging_config_path)
    if train_or_predict == "train":
        run_train_pipeline(params)
    elif train_or_predict == "predict":
        run_test_pipeline(params)

    logger.info("End app")


if __name__ == "__main__":
    pipeline_command()
