# Project 5: Weather Data Analysis

temperatures = [30, 32, 31, 29, 28, 33, 34]

print("Weekly Weather Analysis")
print("-----------------------")

for day, temp in enumerate(temperatures, start=1):
    print(f"Day {day}: {temp}°C")

average_temp = sum(temperatures) / len(temperatures)
print("\nAverage Temperature:", average_temp, "°C")
