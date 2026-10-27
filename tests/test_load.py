import pathlib

import pandas as pd
import pytest
from src.data import (
    load,
)

def test_load_split_invalid_name():
    with pytest.raises(ValueError):
        load.load_split("training")

@pytest.mark.parametrize("split", ["train", "validation", "test"])
def test_load_split_valid_name(split):
    load.load_split(split)

@pytest.mark.parametrize("split", ["train", "validation", "test"])
def test_load_split_return_dataframes(monkeypatch, tmp_path, split):
    for filename in load.DATA_FILES[split]:
        f = pathlib.Path(tmp_path, filename)
        pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}).to_csv(f, index=False)

    monkeypatch.setattr(load, "DATA_DIR", tmp_path)

    result = list(load.load_split(split))
    assert len(result) == len(load.DATA_FILES[split])
    for df in result:
        assert isinstance(df, pd.DataFrame)
        assert df.shape == (3, 2)

def test_load_split_missing_file(monkeypatch, tmp_path):
    monkeypatch.setattr(load, "DATA_DIR", tmp_path)
    with pytest.raises(FileNotFoundError):
        list(load.load_split("train"))






