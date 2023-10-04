# The next_date function takes the date_string parameter in the format of "year-month-day", and uses the add_year function to calculate the next year that this date will occur. 
#Then it returns the value in the same format as it receives the date.

import datetime
from datetime import date

def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        # This gets executed when the above method fails,
        # which means that we're making a Leap Year calculation
        new_date_obj = date_obj.replace(year=date_obj.year + 4)
    return new_date_obj

def next_date(date_string):
    # Convert the argument from string to date object
    date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
    next_date_obj = add_year(date_obj)

    # Convert the datetime object to string,
    # in the format of "yyyy-mm-dd"
    next_date_string = next_date_obj.strftime("%Y-%m-%d")  # Corrected format string
    return next_date_string

today = date.today()  # Get today's date
print("Today:", today)
print("Next Year:", next_date(str(today)))
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01"))  # Should return 2022-01-01
print(next_date("2020-02-29"))  # Should return 2024-02-29
