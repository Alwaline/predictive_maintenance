import pathlib

DATA_FILES = {
    "train": [
        "train_operational_readouts.csv", "train_specifications.csv", "train_tte.csv",
    ],
    "validation": [
        "validation_operational_readouts.csv", "validation_specifications.csv", "validation_labels.csv",
    ],
    "test": [
        "test_operational_readouts.csv", "test_specifications.csv", "test_labels.csv"
    ],
}
PROJECT_DIR = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = pathlib.Path(PROJECT_DIR, "data/row/")