import calendar
from datetime import datetime

"""Python program to find day of the week for a given date.

Also to find todays date, which can be used to find the day
"""

# To find a day of the week.
def find_day(date):
    day = datetime.strptime(date, '%Y-%m-%d').weekday()
    return calendar.day_name[day]

# To find today's date.
def today():
    return str(datetime.date(datetime.now()))

if __name__ == '__main__':
    d = today()
    print("Today is", find_day(d))