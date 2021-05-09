from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default="RandomForestRegressor")
    random_state: int = field(default=2021)
    n_estimators: int = field(default=1000)
