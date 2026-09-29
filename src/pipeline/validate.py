"""
Stage 4: Data Validation.
Checks schema, label values, and feature ranges.
"""

import argparse
import logging
import sys
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("validate")


EXPECTED_COLUMNS = {
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "species",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio",
    "petal_length_bin",
}

VALID_SPECIES = {"setosa", "versicolor", "virginica"}


class DataValidationError(Exception):
    pass


def validate_data(input_path: str) -> None:
    df = pd.read_csv(input_path)
    errors = []

    missing = EXPECTED_COLUMNS - set(df.columns)
    if missing:
        errors.append(f"Missing columns: {sorted(missing)}")

    if not df["species"].isin(VALID_SPECIES).all():
        errors.append("Invalid species values found")

    numeric_ranges = {
        "sepal length (cm)": (0, 10),
        "sepal width (cm)": (0, 10),
        "petal length (cm)": (0, 10),
        "petal width (cm)": (0, 10),
    }

    for col, (low, high) in numeric_ranges.items():
        if not df[col].between(low, high).all():
            errors.append(f"{col} has values outside [{low}, {high}]")

    if errors:
        for error in errors:
            logger.error(error)
        raise DataValidationError("Data validation failed")

    logger.info(
        "Validation passed: %d rows, %d columns",
        len(df),
        len(df.columns),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/iris_features.csv")
    args = parser.parse_args()

    try:
        validate_data(args.input)
    except DataValidationError as exc:
        logger.error(str(exc))
        sys.exit(1)