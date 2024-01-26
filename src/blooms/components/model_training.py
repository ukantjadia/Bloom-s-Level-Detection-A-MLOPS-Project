from blooms import logger
from blooms.entity.config_entity import ModelTrainingConfig
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import MultinomialNB

import pandas as pd
import joblib
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        train_x = train_data[self.config.training_columns]
        train_y = train_data[[self.config.target_columns]]

        # elasticNet = ElasticNet(
        #     alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=34
        # )
        # elasticNet.fit(train_x, train_y)
        # joblib.dump(elasticNet, os.path.join(self.config.root_dir, self.config.el))

        multiNomial = Pipeline(
            [
                (self.config.pipeline_ele_1, TfidfVectorizer()),
                # (self.config.pipeline_ele_2, SMOTE(random_state=12)),
                (self.config.pipeline_ele_3, MultinomialNB()),
            ]
        )
        multiNomial.fit(train_x, train_y)
        joblib.dump(
            multiNomial,
            os.path.join(self.config.root_dir, self.config.multinomial_model_name),
        )
        logger.info(
            f"Model training done! Model saved at {self.config.multinomial_model_name}"
        )
