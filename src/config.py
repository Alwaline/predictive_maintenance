import pathlib
import numpy as np

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
EDGES = np.array([6, 12, 24, 48])
COST = np.array([[0, 7, 8, 9, 10],
                 [200, 0, 7, 8, 9],
                 [300, 200, 0, 7, 8],
                 [400, 300, 200, 0, 7],
                 [500, 400, 300, 200, 0]])
UNKNOWN_CLASS = -1