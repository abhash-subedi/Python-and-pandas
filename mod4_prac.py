import csv
from pathlib import Path

sentence = 'the cat the dog'
count = {}

ROOT_DIR = Path(__file__).resolve().parent
FILEPATH = ROOT_DIR / "orders.csv"

def clean_text(text:str)->list:
    '''cleans sentence given into a list of words'''
    return text.split()

def count_words(text:list)->dict:
    '''function to count occurance of words in text given'''
    for word in text:
        if word in count:
            count[word]+=1
        else:
            count[word] = 1
    return count

def file_prac():
    '''function to readfile and sum one column of given file and 
    also finds average of said column'''
    total = 0
    count = 0
    try:
            with open(FILEPATH, mode= 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total += float(row['price'])
                    count+=1
                avg = total/count
                print(f'total: {total}, average: {avg}')
    except:
        print('file not found')
    
def main():
    file_prac()

if __name__ == '__main__':
    main()
