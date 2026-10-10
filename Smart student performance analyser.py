name = input("Enter student name: ")
marks = []
for i in range(5):
    mark = int(input("Enter subject marks: "))
    marks.append(mark)
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"
print("\nSTUDENT PERFORMANCE REPORT")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Grade:", grade)
