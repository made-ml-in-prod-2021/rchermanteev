from pydantic import BaseModel, validator


class FeaturesToPredict(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: int
    slope: int
    ca: int
    thal: int

    @validator("age")
    def check_age(cls, age_value):
        if not 0 <= age_value <= 120:
            raise ValueError("Unreal age")

        return age_value

    @validator("sex")
    def check_sex(cls, sex_value):
        if sex_value not in [0, 1]:
            raise ValueError("Undefined gender")

        return sex_value
