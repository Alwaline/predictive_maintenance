import pandas as pd
import numpy as np
from src.config import EDGES, UNKNOWN_CLASS


def get_train_class(df: pd.DataFrame, return_df: bool = False) -> pd.DataFrame:

    if any(col not in df.columns for col in ["vehicle_id", "length_of_study_time_step", "time_step", "in_study_repair"]):
        raise ValueError("The dataframe must have columns \"vehicle_id\", \"length_of_study_time_step\", \"time_step\"")

    if not return_df:
        df = df.loc[:, ["vehicle_id", "length_of_study_time_step", "time_step", "in_study_repair"]]

    df = df.sort_values(["vehicle_id", "time_step"]).copy()

    df["tte"] = df["length_of_study_time_step"] - df["time_step"]

    df["class_label"] = np.where(
        ~df["in_study_repair"] & (df["tte"] <= EDGES[-1]),
        UNKNOWN_CLASS,
        (4 - np.searchsorted(EDGES, df["tte"]))
    )

    if return_df:
        return df
    return df[["class_label"]]