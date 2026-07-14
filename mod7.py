import pandas as pd
from pathlib import Path
import numpy as np

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
df = load_titanic_data(FILE_PATH)

def question_1(df: pd.DataFrame) -> None:
    """
    Question 1: finds various attributes of the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
    Returns:
        pd.DataFrame: The first 5 rows of the DataFrame.
    """
    nul_column = df.isnull().sum()
    print(nul_column)
    df['Age'].fillna(df['Age'].mean())
    df.dropna(subset=['Embarked'])
    print(df)

def question_2(df: pd.DataFrame) -> None:
        """changes the sex of Male to male"""
        df["Sex"] = np.where(df["Sex"].str.lower() == "male", 'male', 'Female')

def question_3(df: pd.DataFrame) -> None:
    """converst order date to datetime and creates month and year columns"""
    df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
    df['Month'] = df['order_date'].dt.month
    df['Year'] = df['order_date'].dt.year

def question_4(df: pd.DataFrame) -> None:
     """removes duplicates from the DataFrame"""
     len_before = len(df)
     df = df.drop_duplicates()
     len_after = len(df)
     print(f"Removed {len_before - len_after} duplicates")


