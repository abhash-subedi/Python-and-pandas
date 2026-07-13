from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "expenses_sample.csv"

with open(FILE_PATH, "r") as f:
    data = f.read()

print(data)