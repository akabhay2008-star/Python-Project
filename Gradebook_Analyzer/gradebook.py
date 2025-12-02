"""
------------------------------------------------------------
GRADEBOOK ANALYZER - MINI PROJECT 
Author: Abhay Kumar
Date: 25-Nov-2025
Course: Programming for Problem Solving Using Python
------------------------------------------------------------
"""

import csv
import statistics


# -----------------------------------------------------------
# TASK 3: STATISTICS FUNCTIONS
# -----------------------------------------------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

def find_min_score(marks_dict):
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]


# -----------------------------------------------------------
# TASK 4: GRADE ASSIGNMENT
# -----------------------------------------------------------

def assign_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"   # For marks < 60


# -----------------------------------------------------------
# TASK 2: INPUT METHODS
# -----------------------------------------------------------

def manual_entry():
    marks = {}
    try:
        n = int(input("Enter total number of students: "))
    except ValueError:
        print("Invalid number. Try again.\n")
        return {}

    for _ in range(n):
        name = input("Enter student name: ").strip()
        try:
            score = int(input("Enter marks: "))
        except ValueError:
            print("Invalid marks! Must be an integer.")
            return {}
        marks[name] = score

    return marks


def load_from_csv():
    path = input("Enter CSV file path (example: students.csv): ").strip()

    marks = {}
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)

            if "Name" not in reader.fieldnames or "Marks" not in reader.fieldnames:
                print("ERROR: CSV must contain 'Name' and 'Marks' columns!")
                return {}

            for row in reader:
                name = row["Name"].strip()
                try:
                    score = int(row["Marks"].strip())
                except ValueError:
                    print(f"Invalid marks for student {name}. Must be an integer.")
                    return {}
                marks[name] = score

        print("CSV Loaded Successfully!")

    except FileNotFoundError:
        print("ERROR: File not found. Check name & location.")
        return {}

    return marks


# -----------------------------------------------------------
# TASK 6: PRINT FORMATTED TABLE
# -----------------------------------------------------------

def print_results_table(marks, grades):
    print("\n-------------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("-------------------------------------------")

    for name, score in marks.items():
        print(f"{name:<15}{score:<10}{grades[name]}")

    print("-------------------------------------------\n")


# -----------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------

def main():
    print("\n===========================================")
    print("        Welcome to GradeBook Analyzer")
    print("===========================================\n")

    while True:
        print("Choose Input Method:")
        print("1. Manual Entry")
        print("2. Load from CSV")
        print("3. Exit")

        choice = input("\nEnter option (1/2/3): ").strip()

        # --------------------------
        # TASK 2 – GET DATA
        # --------------------------

        if choice == "1":
            marks = manual_entry()
            if not marks:
                print("No valid data. Try again.\n")
                continue

        elif choice == "2":
            marks = load_from_csv()
            if not marks:
                print("No valid CSV data. Try again.\n")
                continue

        elif choice == "3":
            print("Thank you for using GradeBook Analyzer!")
            break

        else:
            print("Invalid option! Try again.\n")
            continue

        # --------------------------
        # TASK 3 – STATISTICS
        # --------------------------

        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        print("\n===== STATISTICAL SUMMARY =====")
        print(f"Average Score: {avg:.2f}")
        print(f"Median Score : {med}")
        print(f"Highest Score: {max_name} ({max_score})")
        print(f"Lowest Score : {min_name} ({min_score})")
        print("================================\n")

        # --------------------------
        # TASK 4 – GRADE ASSIGNMENT
        # --------------------------

        grades = {name: assign_grade(score) for name, score in marks.items()}

        grade_dist = {
            "A": list(grades.values()).count("A"),
            "B": list(grades.values()).count("B"),
            "C": list(grades.values()).count("C"),
            "D": list(grades.values()).count("D"),
            "F": list(grades.values()).count("F"),
        }

        print("===== GRADE DISTRIBUTION =====")
        for g, count in grade_dist.items():
            print(f"{g}: {count} students")
        print("================================\n")

        # --------------------------
        # TASK 5 – PASS / FAIL USING LIST COMPREHENSION
        # --------------------------

        passed_students = [name for name, score in marks.items() if score >= 40]
        failed_students = [name for name, score in marks.items() if score < 40]

        print("===== PASS / FAIL SUMMARY =====")
        print(f"Passed ({len(passed_students)}): {passed_students}")
        print(f"Failed ({len(failed_students)}): {failed_students}")
        print("================================\n")

        # --------------------------
        # TASK 6 – TABLE OUTPUT
        # --------------------------

        print_results_table(marks, grades)

        repeat = input("Run analysis again? (y/n): ").strip().lower()
        if repeat != "y":
            print("\nThank you for using GradeBook Analyzer!")
            break


# -----------------------------------------------------------
# RUN PROGRAM
# -----------------------------------------------------------

if __name__ == "__main__":
    main()

