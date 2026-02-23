# Exact Age Calculator

from datetime import datetime

# User input
day = int(input("Enter birth day (DD): "))
month = int(input("Enter birth month (MM): "))
year = int(input("Enter birth year (YYYY): "))

# Birth date object
birth_date = datetime(year, month, day)

# Current date
today = datetime.now()

# Difference
difference = today - birth_date

# Calculations
age_years = difference.days // 365
age_months = difference.days // 30
age_days = difference.days
age_hours = difference.days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age_years

# Display
print("\n--- PRECISE AGE DETAILS ---")
print("Current Age:", age_years, "years")
print("Age in Months (approx):", age_months)
print("Age in Days:", age_days)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years until 100:", years_to_100)