from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "expenses_sample.csv"

expenses = []

def save():
    """Saves the current list of expenses to a CSV file."""
    with open(FILE_PATH, "w") as f:
        f.writelines(expenses)


def load():
    """Loads expenses from a CSV file into the expenses list."""
    try:
        with open(FILE_PATH, 'r') as file:
            # .read().splitlines() splits lines cleanly and strips away hidden \r or \n tokens
            lines = file.read().splitlines() 
            
            if not lines:
                print("--- File is completely empty ---")
                return
                
            # Clear previous data so you don't double your list if you press 5 twice
            expenses.clear() 
            
            # Use a manual slice to skip the first header line safely
            # lines[1:] means "start at index 1 and go to the end"
            for line in lines[1:]:
                if line.strip():  # Skip empty rows
                    expenses.append(line + '\n') # Re-add newline for consistency with show_full()
                    
            print(f"--- Successfully loaded {len(expenses)} rows of data! ---")
            
    except FileNotFoundError:
        print(f"--- Error: System cannot find the file at {FILE_PATH} ---")

def show_full():
    """Displays all expenses in the list."""
    for expense in expenses:
        print(expense)
    

def show_summary():
    """Displays a summary of the expenses."""
    summary = {}
    min_amount = 1000000  # Set to a high value to ensure it gets replaced
    max_amount = 0
    no_expenses = len(expenses)
    for expense in expenses:
        date, category, amount,  description = expense.strip().split(',')
        if category not in summary:
            summary[category] = 0
        amount = float(amount)
        summary[category] += amount
        if amount < min_amount:
            min_amount = amount
        if amount > max_amount:
            max_amount = amount
        avg_amount = sum(summary.values()) / no_expenses if no_expenses > 0 else 0
    print(summary)
    print(f"Minimum amount: {min_amount}")
    print(f"Maximum amount: {max_amount}")
    print(f"Average amount: {avg_amount}")

def add(date:str, category:str, amount:float, description:str):
    """"Adds a new expense to the list."""

    expenses.append(f'{date},{category},{amount},{description}\n')
    

def main():
    while True:
        response = input('Enter what you would like to do \n type 1 for adding bill' \
     '\n type 2 for showing all bills \n type 3 for showing summary \n type 4 for save \n type 5 for load \n type 6 to quit \n')
        if response == '1':
            date = input('Enter the date of the bill (YYYY-MM-DD): ')
            category = input('Enter the category of the bill: ')
            amount = float(input('Enter the amount of the bill: '))
            if(amount < 0):
                print('Amount cannot be negative. Please try again.')
                continue
            description = input('Enter a description for the bill: ')
            add(date, category, amount, description)
        elif response == '2':
            show_full()
            
        elif response == '3':
            show_summary()
            
        elif response == '4':
            save()
            
        elif response == '5':
            load()
              # Skip the rest of the loop and prompt for input again
        elif response == '6':
            print('Exiting the program.')
            break
        else:
            print('Invalid option. Please try again.')
        
            main()

if __name__ == "__main__":
    main()