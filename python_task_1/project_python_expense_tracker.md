# Project: Expense Tracker (Command-Line App)

A consolidation project for anyone who has finished **Part 1 — Python Foundations (Modules 1–5)**. You'll build a small but complete command-line program using only standard Python — **no Pandas**. The point is to combine everything from Part 1 into one working application before moving on to data analysis.

> Later, in the Pandas part of the course, you'll rebuild the *summary* piece of this project in a handful of lines. Doing it "by hand" now is what makes that payoff obvious.

---

## What you'll build

A program that runs in the terminal and lets a user track personal expenses. It shows a menu, lets the user add and view expenses, prints spending summaries, and saves/loads everything to a CSV file so the data survives between runs.

A typical session looks like this:

```
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Show summary
4. Save
5. Load
6. Quit
Choose an option: 1

Date (YYYY-MM-DD): 2024-06-10
Category: Food
Amount: 14.50
Description: Lunch
Added: Food $14.50 on 2024-06-10

Choose an option: 3

--- Summary ---
Total spent:        $216.65
Number of expenses: 11
Average expense:    $19.70
Biggest expense:    $60.00 (Utilities)

Spending by category:
  Food           $83.15
  Transport      $31.00
  Entertainment  $60.00
  Utilities      $60.00
```

---

## Skills it exercises (and where each comes from)

| Part of the project | Module it practices |
|---|---|
| Menu text, formatted output, money formatting | Module 1 — basics & f-strings |
| Menu loop, validating the user's choice | Module 2 — control flow |
| Storing expenses as a list of dictionaries; category totals as a dict; comprehensions for summaries | Module 3 — data structures |
| Splitting the program into functions; reading/writing the CSV; handling bad input | Module 4 — functions, files, errors |
| Computing statistics (average, max, spread) | Module 5 — NumPy *(optional stretch)* |

---

## Data format

Store expenses in a CSV file with these columns:

```
date,category,amount,description
2024-06-01,Food,12.50,Lunch at cafe
```

A starter file, **`expenses_sample.csv`**, is provided so your "Load" feature has something to read on day one. In code, each expense is a dictionary:

```python
{"date": "2024-06-01", "category": "Food", "amount": 12.50, "description": "Lunch at cafe"}
```

and the whole dataset is a **list of those dictionaries** — the same shape you'll later meet as a DataFrame.

---

## Build it in milestones

Don't try to write the whole thing at once. Get each milestone working and tested before starting the next.

### Milestone 1 — Menu loop (in memory)
Show the menu, read the user's choice, and react to it in a loop that repeats until they choose Quit. Implement **Add expense** (append a dictionary to a list) and **View all expenses** (print them as a neat table). Data only needs to live in memory for now.
- *Practices:* the `while` loop, `if`/`elif` branching, lists, f-strings.
- *Done when:* you can add a few expenses and see them listed, then quit cleanly.

### Milestone 2 — Summary
Add **Show summary**: total spent, number of expenses, average per expense, the single biggest expense (with its category), and a breakdown of total spending per category.
- *Practices:* dictionaries (category → running total), comprehensions, `sum()`/`max()`.
- *Hint:* build the per-category totals by looping once and using `totals[cat] = totals.get(cat, 0) + amount`.
- *Done when:* the numbers are correct for a handful of expenses you add by hand.

### Milestone 3 — Save and load
Add **Save** (write the list of expenses to a CSV) and **Load** (read a CSV back into the list). Use the built-in `csv` module — `csv.DictWriter` to save and `csv.DictReader` to load.
- *Practices:* file I/O, the `csv` module, converting the `amount` text back into a number on load.
- *Hint:* `csv.DictReader` gives every field as a **string**, so remember `float(row["amount"])`.
- *Done when:* you can save, quit, restart the program, load `expenses_sample.csv`, and see the data.

### Milestone 4 — Make it robust
Handle the things a user will inevitably do wrong, without the program crashing:
- Non-numeric amount (e.g. they type "twelve") → ask again instead of crashing.
- An invalid menu choice (e.g. "9" or "banana") → show a message and re-display the menu.
- Loading a file that doesn't exist → print a friendly message and carry on.
- *Practices:* `try`/`except` with `ValueError` and `FileNotFoundError`.
- *Done when:* you actively try to break it and it refuses to crash.

### Milestone 5 — Stretch goals (optional)
Pick any that interest you:
- **Filter**: view only the expenses in one category.
- **Sort**: view expenses sorted by amount (largest first) using `sorted(..., key=..., reverse=True)`.
- **Monthly view**: total spending per month (extract the month from the date string).
- **Budget warning**: let the user set a monthly budget and warn when a category exceeds it.
- **NumPy stats** (Module 5): put the amounts in a NumPy array and report the mean, max, and standard deviation.

---

## Suggested structure

Organize the program as functions with a `main()` that runs the loop. You don't have to match these exactly, but this is a clean starting shape:

```python
import csv

def load_expenses(filename):
    """Read the CSV and return a list of expense dicts."""

def save_expenses(expenses, filename):
    """Write the list of expense dicts to the CSV."""

def add_expense(expenses):
    """Ask the user for details and append a new expense dict."""

def view_expenses(expenses):
    """Print all expenses as a formatted table."""

def show_summary(expenses):
    """Print totals, average, biggest, and per-category breakdown."""

def main():
    expenses = []
    while True:
        # show menu, read choice, call the right function
        ...

if __name__ == "__main__":
    main()
```

Keeping each feature in its own function is exactly the Module 4 habit: one function, one clear job, returning or printing its result.

---

## When it breaks (debugging tips)

You *will* hit errors — that's normal and part of the exercise. Read the last line of the error message first; it names the problem:

- `ValueError: could not convert string to float` → you tried `float()` on text that isn't a number. Wrap it in `try`/`except`.
- `KeyError: 'amount'` → you asked a dictionary for a key it doesn't have (check spelling and that the CSV header matches).
- `FileNotFoundError` → the filename is wrong or the file isn't in the folder you're running from.
- The program loops forever → your `while` loop has no path that reaches `break` (the Quit option).

---

## Definition of done

Your project is complete when:

- [ ] The menu runs in a loop and quits cleanly.
- [ ] You can add expenses and view them in a readable format.
- [ ] The summary shows total, count, average, biggest expense, and per-category totals — all correct.
- [ ] You can save to a CSV and load it back in a later run.
- [ ] Typing bad input (bad amount, bad menu choice, missing file) never crashes the program.
- [ ] The code is split into functions with a `main()` under `if __name__ == "__main__":`.
- [ ] It runs top to bottom with no leftover errors.

**Deliverable:** a single `expense_tracker.py` file that runs from the terminal, plus your saved `expenses.csv`.

---

## A note on scale

This is deliberately built the "manual" way — looping, counting, and totalling by hand. When you reach the Pandas modules, the entire summary section becomes something like `df.groupby("category")["amount"].sum()`. Keep this project; comparing the two is one of the best ways to see what Pandas actually does for you.
