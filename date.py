from datetime import datetime, timedelta

# 1. Get current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# 2. Get only the current date
current_date = current_datetime.date()
print("Current date:", current_date)

# 3. Get only the current time
current_time = current_datetime.time()
print("Current time:", current_time)

# 4. Format date and time in a specific way (e.g., 'YYYY-MM-DD HH:MM:SS')
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)

# 5. Adding and subtracting days from the current date
days_to_add = 5
future_date = current_datetime + timedelta(days=days_to_add)
print(f"Date after adding {days_to_add} days:", future_date.date())

days_to_subtract = 3
past_date = current_datetime - timedelta(days=days_to_subtract)
print(f"Date after subtracting {days_to_subtract} days:", past_date.date())

# 6. Compare two dates
another_date = datetime(2024, 12, 25)  # Example: Christmas 2024
if current_datetime.date() < another_date.date():
    print("Today's date is before Christmas 2024.")
else:
    print("Today's date is on or after Christmas 2024.")

# 7. Difference between two dates
difference = another_date - current_datetime
print(f"Days until Christmas 2024: {difference.days} days")

# 8. Creating a specific date and time
specific_datetime = datetime(2023, 1, 1, 10, 30, 45)  # Jan 1, 2023, 10:30:45
print("Specific date and time:", specific_datetime)

# 9. Check if a year is a leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 10. Parse a string into a datetime object
date_string = "2024-10-11 15:45:30"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime from string:", parsed_datetime)
