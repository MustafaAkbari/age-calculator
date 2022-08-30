import datetime as dt
print("Enter your birth date in this format, yyyy-mm-dd")
birth_date = input("What is your birth date: ").split("-")
year, month, day = birth_date
updated_year = int(year)
updated_month = int(month)
updated_day = int(day)
present_year = dt.date.today().year
present_month = dt.date.today().month
present_day = dt.date.today().day
year_age = present_year - updated_year
month_age = present_month - updated_month
day_age = present_day - updated_day
if month_age <= 0:
    print(f"You have {abs(month_age)} month and {day_age} to become {year_age} years old.")
else:
    print(f"You have {year_age} years, {month_age} months and {day_age} days")











