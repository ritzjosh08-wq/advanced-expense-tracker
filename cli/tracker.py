import json
import os
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(__file__),"expenses.json")

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Save file is corrupted. Starting fresh.")
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def show_menu():
    print("\n===== Expense tracker =====")
    print("1. Add expense")
    print("2. View expense")
    print("3. Total spent")
    print("4. Exit")


def add_expenses(expenses):
    while True:
        try:
            amount = float(input("Amount (£): "))
            if amount <= 0:
                print("Amount must be more than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

    category = input("Category (Food, Travel, Entertainment, Rent...): ").strip().title()
    note = input("Note: ").strip()
    expense_date = input("Date (YYYY-MM-DD): ").strip()

    if expense_date == "":
        expense_date = date.today().isoformat()

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": expense_date,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print("\n--- Your expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} - {exp['category']} - £{exp['amount']:.2f} - {exp['note']}")


def total_spent(expenses):
    total = 0
    for exp in expenses:
        total += exp['amount']
    print(f"Total spent: £{total:.2f}")


def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_spent(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

