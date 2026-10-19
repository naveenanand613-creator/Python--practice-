students = {
    "Naveen": [85, 90, 78],
    "Rahul": [70, 82, 75],
    "Meenakshi": [95, 92, 98],
    "Anil": [65, 72, 68]
}
averages = {}
print("STUDENT RESULT DASHBOARD")
print("------------------------")
for name, marks in students.items():
    average = sum(marks) / len(marks)
    averages[name] = average
    print(name, "- Average:", round(average, 2))
top_student = max(averages, key=averages.get)
print("------------------------")
print("Top Performer:", top_student)
print("Highest Average:", round(averages[top_student], 2))
print("Class Average:", round(sum(averages.values()) / len(averages), 2))
