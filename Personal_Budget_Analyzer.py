expenses = {}
count = int(input("How many expenses do you have? "))
for i in range(count):
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    expenses[category] = amount
total = sum(expenses.values())
average = total / len(expenses)
highest = max(expenses, key=expenses.get)
print("\nPERSONAL BUDGET REPORT")
for category, amount in expenses.items():
    print(category, ":", amount)
print("Total Spending:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Highest Amount:", expenses[highest])
