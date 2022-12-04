import calendar

print("Welcome to Calendar")

year = 2022
month = 0

for i in range(12):
    month += 1
    print(calendar.month(year, month))

print("Next year 2023")