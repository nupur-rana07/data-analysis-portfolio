# Project 2: Healthcare Data Analysis

patients = [
    {"name": "Amit", "age": 45, "disease": "Diabetes"},
    {"name": "Neha", "age": 30, "disease": "Asthma"},
    {"name": "Ravi", "age": 60, "disease": "Heart Disease"},
    {"name": "Pooja", "age": 25, "disease": "Flu"}
]

print("Healthcare Data Analysis")
print("------------------------")

for patient in patients:
    print(f"Name: {patient['name']}, Age: {patient['age']}, Disease: {patient['disease']}")

average_age = sum(p["age"] for p in patients) / len(patients)
print("\nAverage Patient Age:", average_age)
