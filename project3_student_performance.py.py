# Project 3: Student Performance Analysis

students = {
    "Nupur": 85,
    "Rahul": 78,
    "Sneha": 92,
    "Aman": 67
}

print("Student Performance Report")
print("--------------------------")

for name, marks in students.items():
    print(f"{name} scored {marks} marks")

average_marks = sum(students.values()) / len(students)
print("\nAverage Marks:", average_marks)
