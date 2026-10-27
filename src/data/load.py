import pathlib

import requests
from tqdm import tqdm
import pandas as pd

from src.config import PROJECT_DIR, DATA_DIR, DATA_FILES

def download_data():
    """
    Download data from researchdata.se
    """

    print("Base data directory: ", pathlib.Path(PROJECT_DIR, DATA_DIR))

    files = [file for split in DATA_FILES.values() for file in split]

    # files = ["train_operational_readouts.csv", "train_specifications.csv", "train_tte.csv",
    #          "validation_operational_readouts.csv", "validation_specifications.csv", "validation_labels.csv",
    #          "test_operational_readouts.csv", "test_specifications.csv", "test_labels.csv"]

    print("Next files will be downloaded: ", files)

    print("Loading data...")
    print("-" * 80)
    for file in files:
        print("Loading file: ", file)

        path = pathlib.Path(DATA_DIR, file)
        if not path.exists():
            response = requests.get(f"https://api.researchdata.se/dataset/2024-34/3/file/data/{path.name}", stream=True)

            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                print(f"Total size: {round(total_size / 1024 / 1024, 2)} MB")
                block_size = 1024

                with tqdm(total=total_size, unit='B', unit_scale=True, desc=file) as pbar:
                    with open(path, "wb") as f:
                        for data in response.iter_content(chunk_size=block_size):
                            if data:
                                f.write(data)
                                pbar.update(len(data))
                        print("File saved: ", path.name)

            else:
                print("Response code: ", response.status_code)
        else:
            print("File exists: ", path.name)
        print("-" * 80)

    print("Done!")


def load_split(split):
    if split not in ["train", "validation", "test"]:
        raise ValueError("Split must be one of 'train', 'validation' or 'test'")

    return (
        pd.read_csv(pathlib.Path(DATA_DIR, file))
        for file in DATA_FILES[split]
    )

if __name__ == "__main__":
    download_data()
