"""
The calendar module allows you to output calendars and provides additional useful functions for them.
"""
# find the day on december 3rd 2022?
import calendar

print(calendar.TextCalendar(firstweekday=0).formatyear(2022)) # generate plain text calendars.
print(calendar.weekday(2022,12,3)) # gives weekday in given year month day
print(calendar.day_name[calendar.weekday(2022,12,3)]) #return day_name on the given name


