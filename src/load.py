import pathlib

import requests
from tqdm import tqdm

data_dir = "data/row"

print("Base data directory: ", data_dir)

files = ["train_operational_readouts.csv", "train_specifications.csv", "train_tte.csv",
         "validation_operational_readouts.csv", "validation_specifications.csv", "validation_labels.csv",
         "test_operational_readouts.csv", "test_specifications.csv", "test_labels.csv"]

print("Next files will be downloaded: ", files)

print("Loading data...")
print("-" * 80)
for file in files:
    print("Loading file: ", file)

    path = pathlib.Path(data_dir, file)
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
