"""
Stage 2: Data Preprocessing.
Cleans raw data and writes a processed dataset.
"""

import argparse
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("preprocess")


NUMERIC_COLS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]


def preprocess_data(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    before = len(df)
    df = df.drop_duplicates()
    logger.info("Dropped %d duplicate rows", before - len(df))

    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    df = df.dropna(subset=["species"])

    if "collected_at" in df.columns:
        df = df.drop(columns=["collected_at"])

    df.to_csv(output_path, index=False)
    logger.info("Preprocessed %d rows -> %s", len(df), output_path)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/iris_raw.csv")
    parser.add_argument("--output", default="data/processed/iris_preprocessed.csv")
    args = parser.parse_args()
    preprocess_data(args.input, args.output)