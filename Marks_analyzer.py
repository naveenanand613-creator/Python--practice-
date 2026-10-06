def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return total, average, highest, lowest
marks = [78, 85, 92, 67, 88]
total, average, highest, lowest = analyze_marks(marks)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
