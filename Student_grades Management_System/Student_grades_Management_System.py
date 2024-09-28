#Course: CIS 103
#Instructor: Md Ali
#Group project (Group:03)
#Date: 09/27/2024

# Task: Student Grades Management System:

# Create a dictionary with Student_grades:
Student = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 60,
    "Diana": 78
   }

# Calculate the average grade of all Students in the class

if len(Student) > 0:
    total_grades = sum(Student.values())  # Get the sum of all grades
    num_students = len(Student)            # Get the number of students
    average_grade = total_grades / num_students  # Calculate the average

    # Print the average grade of class
    print("Average grade of all students:", average_grade)
else:
    print("No students available to calculate the average grade.")

# Add features such as grade categorization (e.g., A, B, C) and handling missing data:
def categorize_grade(grade):

    if grade is None:
        return 'N/A'  # Not applicable for missing grades
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Find the student with the highest and lowest grades:
def find_highest_lowest_grades(students):

    if not students:
        print("No students available.")
        return

    # Initialize variables to store the highest and lowest grades
    highest_student = max(students, key=students.get)
    lowest_student = min(students, key=students.get)

    # Print the results
    print(f"Student with the highest grade: {highest_student} ({students[highest_student]})")
    print(f"Student with the lowest grade: {lowest_student} ({students[lowest_student]})")

# Display all students' grades with their categories.
def display_grades(students):
    
    if not students:
        print("No grades to display.")
        return
    
    print("\nStudent Grades:")
    for name, grade in students.items():
        category = categorize_grade(grade)
        if grade is None:
            print(f"{name}: Missing Grade - Grade Category: {category}")
        else:
            print(f"{name}: {grade} - Grade Category: {category}")

# Example usage
display_grades(Student)          # Display all grades
find_highest_lowest_grades(Student)  # Find and print highest and lowest grades

