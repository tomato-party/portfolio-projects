"""Fire damage-scale prediction with LightGBM.

This script is a cleaned portfolio version of the original competition code.
Raw CSV files are excluded from the public repository; place the integrated
fire dispatch dataset next to this file before running.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import LabelEncoder

TARGET_AMOUNT_COLUMN = "PRPT_DAM_AMT"
DROP_COLUMNS = ["WRINV_NO", TARGET_AMOUNT_COLUMN]
TARGET_COLUMN = "fire_scale"


def read_csv_with_fallback(path: Path) -> pd.DataFrame:
    for encoding in ("utf-8-sig", "utf-8", "cp949"):
        try:
            return pd.read_csv(path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("csv", b"", 0, 1, f"Could not decode {path}")


def add_damage_scale(df: pd.DataFrame) -> pd.DataFrame:
    q33 = df[TARGET_AMOUNT_COLUMN].quantile(0.33)
    q66 = df[TARGET_AMOUNT_COLUMN].quantile(0.66)

    def scale(damage: float) -> str:
        if damage <= q33:
            return "C"
        if damage <= q66:
            return "B"
        return "A"

    out = df.copy()
    out[TARGET_COLUMN] = out[TARGET_AMOUNT_COLUMN].apply(scale)
    return out.drop(columns=[col for col in DROP_COLUMNS if col in out.columns])


def preprocess(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, list[str], LabelEncoder]:
    numeric_features = df.select_dtypes(include=np.number).columns.tolist()
    categorical_features = df.select_dtypes(include="object").columns.tolist()

    if TARGET_COLUMN in categorical_features:
        categorical_features.remove(TARGET_COLUMN)

    for col in numeric_features:
        df[col] = df[col].fillna(df[col].median())

    for col in categorical_features:
        df[col] = df[col].fillna(df[col].mode().iloc[0]).astype("category")

    label_encoder = LabelEncoder()
    y = pd.Series(label_encoder.fit_transform(df[TARGET_COLUMN]), name=TARGET_COLUMN)
    x = df.drop(columns=[TARGET_COLUMN])
    return x, y, categorical_features, label_encoder


def train_model(x: pd.DataFrame, y: pd.Series, categorical_features: list[str]) -> RandomizedSearchCV:
    model = lgb.LGBMClassifier(random_state=42)
    param_dist = {
        "n_estimators": [500, 1000, 1500],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [7, 10, 15],
        "num_leaves": [30, 40, 50],
        "reg_alpha": [0.1, 0.5, 1.0],
        "reg_lambda": [0.1, 0.5, 1.0],
    }
    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_dist,
        n_iter=10,
        scoring="accuracy",
        cv=3,
        random_state=42,
        n_jobs=-1,
    )
    search.fit(x, y, categorical_feature=categorical_features)
    return search


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="fire_dispatch_integrated.csv", help="Path to the fire dispatch CSV file")
    args = parser.parse_args()

    df = add_damage_scale(read_csv_with_fallback(Path(args.data)))
    x, y, categorical_features, label_encoder = preprocess(df)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    search = train_model(x_train, y_train, categorical_features)
    best_model = search.best_estimator_
    y_pred = best_model.predict(x_test)

    print("Best parameters:")
    print(search.best_params_)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

    actual = label_encoder.inverse_transform(y_test)
    predicted = label_encoder.inverse_transform(y_pred)
    print(classification_report(actual, predicted, target_names=label_encoder.classes_))
    print(pd.DataFrame(confusion_matrix(actual, predicted, labels=label_encoder.classes_)))


if __name__ == "__main__":
    main()