# Project 4: Financial Data Analysis

expenses = {
    "Rent": 12000,
    "Food": 5000,
    "Transport": 3000,
    "Internet": 1000
}

print("Monthly Expense Report")
print("----------------------")

total_expense = 0
for item, cost in expenses.items():
    print(f"{item}: ₹{cost}")
    total_expense += cost

print("\nTotal Monthly Expense: ₹", total_expense)
