import pandas as pd
import catboost


def get_validation_last(df: pd.DataFrame) -> pd.DataFrame:
    df_last = df.groupby("vehicle_id").tail(1)

    assert df_last.shape[0] == df["vehicle_id"].nunique()

    return df_last


def build_train_table(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, pd.Series, pd.DataFrame]:
    df_filter = df[df["class_label"] >= 0]
    X = df_filter.drop(columns=["class_label", "vehicle_id", "in_study_repair", "length_of_study_time_step", "tte"])
    y = df_filter["class_label"]
    sizes = df_filter.groupby("vehicle_id").transform("size")
    groups = df_filter["vehicle_id"]
    assert X.shape[0] == y.shape[0] == sizes.shape[0] == groups.shape[0]
    return X, y, groups, 1 / sizes


def build_eval_table(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    df_last = get_validation_last(df)
    X = df_last.drop(columns=["class_label", "vehicle_id"])
    y = df_last["class_label"]
    vehicle_ids = df_last["vehicle_id"]
    return X, y, vehicle_ids


def train_catboost(X, y, weights=None, **params):
    cat_features = X.select_dtypes(str).columns.tolist()
    model = catboost.CatBoostClassifier(**params)

    model.fit(X, y, sample_weight=weights, cat_features=cat_features)

    return model

