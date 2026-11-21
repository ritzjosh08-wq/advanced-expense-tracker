import os
from datetime import date

from expense_tracker import ExpenseTracker
from models import Expense 

DATA_FILE = os.path.join(os.path.dirname(__file__),"expenses.json")

def show_menu():
    print("\n===== Expense tracker =====")
    print("1. Add expense")
    print("2. view expense")
    print("3. Total spent")
    print("4. Total by category")
    print("5. Exit")

def ask_amount() -> float:
    while True:
        try:
            amount = float(input("Amount (£): "))
            if amount <= 0:
                print("Amount must be more than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number, e.g 12.50")

def ask_expense() -> Expense:
    amount = ask_amount()
    category = input("category (Food, travel,Rent...):").strip().title()
    note = input("Note:").strip()
    date_input = input("Date (YYYY-MM-DD), press Enter for today):").strip()

    if date_input =="":
        date_input = date.today().isoformat()

    return Expense(amount=amount, category=category, note=note, date=date_input)

def view_expenses(tracker: list[Expense]) -> None:
    if not tracker.expenses:
        print("No expenses yet.")
        return

    print("\n===== Expenses =====")
    for i, exp in enumerate(tracker.expenses, start=1):
        print(f"{i}. {exp}")


def show_categories(tracker: ExpenseTracker) -> None:
    if not tracker.expenses:
        print("No expenses yet.")
        return

    print("\n===== Total by category =====")
    totals = tracker.total_by_category()
    if not totals:
        print("No expenses yet.")
        return

    print("\n----- Spending by category -----")
    for category, amount in sorted(totals.items(), keys=lambda item: item [1], reverse=True):
        print(f"{category:<15} £{amount:.2f}")

def main() -> None:
    tracker = ExpenseTracker(DATA_FILE)

    while True:
        show_menu()
        choice = input("Enter your choice (1-5):")

        if choice == "1":
            tracker.add(ask_expense())
            print("Expense added and saved!")
        elif choice == "2":
            view_expenses(tracker)
        elif choice == "3":
            print(f"\n Total spent £{tracker.total():.2f}")
        elif choice == "4":
            show_categories(tracker)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
main()

