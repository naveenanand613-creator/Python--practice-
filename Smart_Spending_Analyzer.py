expenses = {
    "Food": 250,
    "Travel": 150,
    "Shopping": 800,
    "Snacks": 100,
    "Entertainment": 400
}
total = sum(expenses.values())
average = total / len(expenses)
highest = max(expenses, key=expenses.get)
print("SMART SPENDING ANALYZER")
print("-----------------------")
for category, amount in expenses.items():
    print(category, ":", amount)
print("-----------------------")
print("Total Spending: ₹", total)
print("Average Spending: ₹", average)
print("Highest Expense:", highest)
print("Amount: ₹", expenses[highest])
if total > 1500:
    print("Alert: Your spending is high!")
else:
    print("Good job! Your spending is under control.")
