numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
total = sum(numbers)
average = total / len(numbers)
highest = max(numbers)
lowest = min(numbers)
sorted_numbers = sorted(numbers)
above_average = []
for number in numbers:
    if number > average:
        above_average.append(number)
print("\nMINI DATA ANALYZER")
print("Original Data:", numbers)
print("Sorted Data:", sorted_numbers)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest Value:", highest)
print("Lowest Value:", lowest)
print("Values Above Average:", above_average)
print("Count Above Average:", len(above_average))
