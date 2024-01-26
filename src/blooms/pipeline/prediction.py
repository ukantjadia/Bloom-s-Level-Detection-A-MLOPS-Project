import joblib
from pathlib import Path


class PredictionPipeline:
    def __init__(self) -> None:
        self.model = joblib.load(
            Path("artifacts/model_training/multinomial_model.joblib")
        )

    def predicter(self, data):
        prediction = self.model.predict([data])
        return prediction
