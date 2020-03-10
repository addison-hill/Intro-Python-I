"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# print out a calender based on arguments...if no args print todays month...if one arg assume month

# Functions
# If user types in wrong format


def usage_statement():
    print('The program expects month to be in format <MM>\nand year to be in format <YYYY>')


def month_is_valid(m):
    if m <= 12 and m >= 1:
        return True
    else:
        return False


# Determine how many args are sent and base your calendar off them
arg_len = len(sys.argv)

if arg_len == 3:
    # User specifies month and year, render calendar for that month and year
    month = int(sys.argv[1])
    year = int(sys.argv[2])

    if month_is_valid(month):
        # 3 is width of the date columns, 1 is number of lines each week will use
        print(calendar.month(year, month, 3, 1))
    else:
        print(usage_statement())

elif arg_len == 2:
    # User only has 1 arg, we are going to assume it is month and use this year from datetime
    month = int(sys.argv[1])
    year = datetime.today().year

    if month_is_valid(month):
        print(calendar.month(year, month, 3, 1))
    else:
        print(usage_statement())

elif arg_len == 1:
    # User did not give any args so we will use todays months and year from datetime
    month = datetime.today().month
    year = datetime.today().year

    print(calendar.month(year, month, 3, 1))

else:
    # Just print our usage statement letting user know what format we expect
    print(usage_statement())
