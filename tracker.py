# Name : Abhay Kumar
# Date : 10th November 2025
# Project Title: Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")

# Calorie Tracker Program

meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals do you want to enter? "))

for i in range(num_meals):
    meal = input("Enter meal name: ")
    calories = float(input("Enter calories for " + meal + ": "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

#Task 1: Total and Average Calculation

total = sum(calorie_amounts)
average = total / num_meals

limit = float(input("Enter your daily calorie limit: "))

# Task 2: Limit Check

if total > limit:
    print("Warning! You have gone over your calorie limit.")
else:
    print("Good job! You are within your calorie limit.")

# Task 3: Report Generation

print("\nMeal Name\tCalories")
print("--------------------------")

for i in range(num_meals):
    print(meal_names[i], "\t", calorie_amounts[i])

print("--------------------------")
print("Total:\t\t", total)
print("Average:\t", round(average, 2))

# Task 4: Save Report to File

save = input("\nDo you want to save this report to a file? (yes/no): ")

if save.lower() == "yes":
    import datetime
    time_now = datetime.datetime.now()
    file = open("calorie_report.txt", "w")

    file.write("Calorie Report - " + str(time_now) + "\n\n")
    file.write("Meal Name\tCalories\n")
    file.write("--------------------------\n")

    for i in range(num_meals):
        file.write(meal_names[i] + "\t" + str(calorie_amounts[i]) + "\n")

    file.write("--------------------------\n")
    file.write("Total:\t" + str(total) + "\n")
    file.write("Average:\t" + str(round(average, 2)) + "\n")

    if total > limit:
        file.write("Status: Over Limit\n")
    else:
        file.write("Status: Within Limit\n")

    file.close()
    print("Report saved as 'calorie_report.txt'")
else:
    print("Report not saved.")
