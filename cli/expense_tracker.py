import json
from math import exp
import os
import os

from models import Expense 


class ExpenseTracker:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.expenses: list[Expense] = self.load()

    def load(self) -> list[Expense]:
        if not os.path.exists(self.data_file):
            return []

        try:
            with open(self.data_file,"r") as file:
                data = json.load(file)
                return [Expense.from_dict(item) for item in data]
        except json.JSONDecoderError:
            print("Save file is corrupted. starting fresh.")
            return []

    def save(self) -> None:
        with open(self.data_file, "w") as file:
            json.dump([expense.to_dict() for expense in self.expenses], file, indent=4)

    def add(self,expense: Expense) -> None:
        self.expenses.append(expense)
        self.save()

    def total(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def total(Self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def total_by_category(self, category: str) -> float:
        totals = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category,0) + expense.amount
        return totals
        




