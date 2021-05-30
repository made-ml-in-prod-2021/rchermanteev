from dataclasses import dataclass, field
from typing import List


@dataclass()
class TrainingParams:
    model_type: str = field(default="RandomForestRegressor")
    random_state: int = field(default=2021)
    n_estimators: int = field(default=1000)
    metrics_list: List[str] = field(default="accuracy_score")
