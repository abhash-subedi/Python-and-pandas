import csv
sentence = 'the cat the dog'
count = {}
FILEPATH = 'orders(1).csv'
def clean_text(text:str)->list:
    return text.split()
def count_words(text:list)->dict:
    
    for word in text:
        if word in count:
            count[word]+=1
        else:
            count[word] = 1
    return count
def print_report():
    return count
def word_count(text:str)->dict:
    words = text.split()
    
def file_prac():
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
