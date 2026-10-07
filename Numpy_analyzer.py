def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    print("Numbers:", numbers)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
numbers = [10, 25, 15, 40, 30]
analyze_numbers(numbers)
