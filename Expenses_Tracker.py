expenses = {
    "Food": 250,
    "Travel": 120,
    "Shopping": 300,
    "Snacks": 150
}

total = sum(expenses.values())

print("Expense Details")

for category, amount in expenses.items():
    print(category, ":", amount)

print("Total Expense:", total)
print("Average Expense:", total / len(expenses))
