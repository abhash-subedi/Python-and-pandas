import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).parent
FILE_PATH_titanic = ROOT_DIR / "titanic.csv"
FILE_PATH_orders = ROOT_DIR/ "orders.csv"

#question asked for function that can show various attributes of titanic dataset 
def attributes_of_titanic(filepath: Path) -> str:
    """returns various atrributes of given dataframe"""
    df = pd.read_csv(filepath)
    return(f'the shape of the dataframe is {df.shape}, the column names are {df.columns},' 
           f'the data type of the columns are {df.dtypes}, the description of dataframe is {df.describe()}')

# question asked for a function that reads select columns from dataset
def bestselling_products(filepath: Path) -> int:
    """shows sum and quantity of orders placed by reading from dataset"""
    df = pd.read_csv(filepath)
    sum = df['price'].sum()
    best_selling = df.sort_values(by='price', ascending=False)
    print(f'the sum of the dataframe is: {sum}')
    print(f'the table ordered by best selling is as follows: {best_selling.head()}')

# question asked for function which that can show people that had first class tickets and survived
def survived(filepath: Path) -> str:
    """this function prints people with first class tickets that survived"""
    df = pd.read_csv(filepath)
    people_of_intrest = df[(df['Pclass']==1) & (df['Survived']==1)][['Name', 'Age']]
    return people_of_intrest

def main():
    print(attributes_of_titanic(FILE_PATH_titanic))
    print(bestselling_products(FILE_PATH_orders))
    print(survived(FILE_PATH_titanic))

if __name__=='__main__':
    main()