from dataclasses import dataclass

from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class TestingPipelineParams:
    test_data_path: str
    output_model_path: str
    predicts_path: str
    transformer_params_path: str
    logging_config_path: str


TestingPipelineParamsSchema = class_schema(TestingPipelineParams)


def read_test_params(path: str) -> TestingPipelineParams:
    with open(path, "r") as input_stream:
        schema = TestingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
