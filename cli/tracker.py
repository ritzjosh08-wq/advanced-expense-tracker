Expenses = []
def show_menu():
    print("\n===== Expense tracker =====")
    print("1. Add expense")
    print("2. view expense")
    print("3. Total spent")
    print("4. Exit")

def add_expenses(expenses):
    amount = float(input("Amount (£): "))
    category = input("category (Food,Travel,Entertainment,Rent...):")
    note = input("Note: ")
    date = input("Date (YYYY-MM-DD):")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date,
    }
    expenses.append(expense)
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
    while True:
        show_menu()
        choice = input("Enter your choice (1-4):")
        if choice == '1':
            add_expenses(Expenses)
        elif choice == '2':
            view_expenses(Expenses)
        elif choice == '3':
            total_spent(Expenses)
        elif choice =='4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice , try again.")


main()

