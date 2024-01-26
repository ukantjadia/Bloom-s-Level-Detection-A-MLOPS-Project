from sklearn.metrics import (
    accuracy_score,
    classification_report,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from urllib.parse import urlparse
from sklearn.preprocessing import LabelEncoder
from blooms import logger
from pathlib import Path
from blooms.entity.config_entity import ModelEvaluationConfig
from blooms.utils.common import save_json
import mlflow
import mlflow.sklearn
import joblib
import pandas as pd


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_matrix(self, actual, pred):
        rmse = mean_squared_error(actual, pred)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        acc = accuracy_score(actual, pred)
        report = classification_report(actual, pred)
        return rmse, mae, r2, acc, report

    def log_into_mlflow(self):
        encoder = LabelEncoder()
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(filename=self.config.model_path)

        test_x = test_data[self.config.training_columns].tolist()
        test_y = test_data[self.config.target_column].tolist()

        mlflow.set_registry_uri(self.config.mlflow_URI)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2, acc, report) = self.eval_matrix(
                encoder.fit_transform(test_y),
                encoder.fit_transform(predicted_qualities),
            )
            scores = {"rmse": rmse, "mae": mae, "r2": r2, "accuracy": acc}
            logger.info(
                f"+++++++++++++++++\n\nthis is the matrix \n {scores}\n\n")
            save_json(path=Path(self.config.metric_file_name), data=scores)
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("accuracy", acc)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="NB Multinomial"
                )
                logger.info(
                    f"Model evaluation is done! model logged to given uri {self.config.mlflow_URI}")
            else:
                mlflow.sklearn.log_model(model, "model")
                logger.info(f"Model evaluation is done! model logged locally")
