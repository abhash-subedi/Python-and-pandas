from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "expenses_sample.csv"

def save(date:str, category:str, amount:float, description:str):
    with open(FILE_PATH, "w") as f:
        f.write(f'{date}, {category}, {amount}, {description}\n')
        