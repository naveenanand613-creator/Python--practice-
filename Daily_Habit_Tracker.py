habits = ["Study Python", "Exercise", "Read a Book", "Drink Enough Water"]
completed = 0
print("DAILY HABIT TRACKER")
for habit in habits:
    status = input("Did you complete " + habit + "? (yes/no): ").lower()
    if status == "yes":
        completed += 1
percentage = completed / len(habits) * 100
print("\nDAILY SUMMARY")
print("Total Habits:", len(habits))
print("Completed:", completed)
print("Remaining:", len(habits) - completed)
print("Completion:", round(percentage, 2), "%")
if percentage == 100:
    print("Excellent! All habits completed!")
elif percentage >= 50:
    print("Good progress! Keep going!")
else:
    print("Tomorrow is another chance to improve!")
  
