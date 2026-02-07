# Project 1: Business Sales Analysis

sales = [
    {"product": "Laptop", "units_sold": 10, "price": 50000},
    {"product": "Mobile", "units_sold": 25, "price": 20000},
    {"product": "Tablet", "units_sold": 15, "price": 30000},
    {"product": "Headphones", "units_sold": 40, "price": 2000}
]

print("Business Sales Report")
print("---------------------")

total_revenue = 0

for item in sales:
    revenue = item["units_sold"] * item["price"]
    total_revenue += revenue
    print(
        f"Product: {item['product']}, "
        f"Units Sold: {item['units_sold']}, "
        f"Revenue: ₹{revenue}"
    )

print("\nTotal Business Revenue: ₹", total_revenue)
