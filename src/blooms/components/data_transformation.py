from sklearn.model_selection import train_test_split
from blooms.entity.config_entity import DataTransformationConfig
from blooms import logger
from nltk.tokenize import word_tokenize
from tqdm import tqdm

import os
import pandas as pd
import nlpaug.augmenter.word as naw


class DataTrnsformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def data_preprocessing(self):
        df = pd.read_csv(self.config.data_path, index_col=None)
        df["Text"] = df["Text"].str.strip()
        df["Text"] = df["Text"].str.lower()
        df.to_csv(self.config.clean_data_path, index=False)

    def augment_text(self,text):
        """
        augmented each Text input 3 times with following parameter with nlpaug library

        ```ContextualWordEmbsAug(model_path="bert-base-uncased", action="insert")```

        before augmendatation data shape : 600,2
        total 6 unique calsses 100 each

        augmented data shape : 1800,2
        total 6 unique classes 300 each
        """
        aug = naw.ContextualWordEmbsAug(model_path="bert-base-uncased", action="insert")
        augmented_text = aug.augment(text)
        return augmented_text

    def augment_rows(self,row):
        augmented_texts = [self.augment_text(row["Text"]) for _ in range(3)]
        text_list = [text for text in augmented_texts]
        level_list = [row["Level"]] * 3
        return {"Text": text_list, "Level": level_list}

    def data_augmentation(self):
        df = pd.read_csv(self.config.clean_data_path, index_col=None)
        augmented_data = []
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Augmenting Text"):
            augmented_data.append(self.augment_rows(row))
        augmented_data_flat = [
            {"Text": Text, "Level": Level}
            for row in augmented_data
            for Text, Level in zip(row["Text"], row["Level"])
        ]
        augmented_df = pd.DataFrame(augmented_data_flat)
        augmented_df.to_csv(self.config.augmented_data_path)
        logger.info(
            f"Done the augmentation! Saving the augmented data file at: {self.config.augmented_data_path}"
        )

    def tokenization(self):
        df = pd.read_csv(self.config.augmented_data_path, index_col=0)
        df["Text"] = df["Text"].apply(lambda x: x[2:-2])
        df = df.drop(df[df["Text"].str.contains(r"\.{2,}", regex=True)].index)
        df["Tokens"] = [word_tokenize(text) for text in df["Text"]]
        df = df.sample(frac=1, random_state=1).reset_index(drop=True)

        df.to_csv(self.config.new_data_path, index=False)
        logger.info(
            f"Done the tokenization! Saving the final cleaned file at: {self.config.new_data_path}"
        )

    def train_test_splitting(self):
        data = pd.read_csv(self.config.new_data_path)
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info(
            f"Done the Splitting! Saving the train and test  file at: {self.config.root_dir}"
        )
        logger.info(f"Splited data into training and testing sets")
        logger.info(f'training shape: {train.shape}')
        logger.info(f'testing shape: {test.shape}')
