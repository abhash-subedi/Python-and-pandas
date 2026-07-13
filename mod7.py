import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "titanic.csv"

def load_titanic_data(file_path: Path = FILE_PATH) -> pd.DataFrame:
    """
    Load the Titanic dataset from a CSV file.

    Args:
        file_path (Path): The path to the CSV file. Defaults to FILE_PATH.
    Returns:
        pd.DataFrame: A DataFrame containing the Titanic dataset.
    """
    return pd.read_csv(file_path)