"""
A date in Python is not a data type of its own, but we can import a module named datetime to work 
with dates as date objects.

"""

import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.time()) # current time of system
print(x.now())# current date time of system

# strftime() method for formatting date objects into readable strings.
print(x.strftime("%A")) # return day name

print(x.strftime("%B")) # returns month

#strptime() method for formatting the given string(date) into desire format


#Create a date object:
y = datetime.datetime(2020,1,15)
print(y)
print(y.strftime("%A")) 
print(y.strftime("%B"))
print(y.strftime("%d"))
print(y.strptime("21 june 2018","%d %B %Y")) # covert given date in YYYY-MM-DD hh:min:sec

print(y.strptime("21 june, 2018","%d %B, %Y")) # covert given date in YYYY-MM-DD hh:min:sec


# convert input string in format Sun 10 May 2015 13:54:36 -0700 
#'%a %d %b %Y %H:%M:%S %z'
# z = input()
# y = input()
c1 = datetime.datetime.strptime('Sun 10 May 2015 13:54:36 -0700', '%a %d %B %Y %H:%M:%S %z')

print(c1)
print(c1.second)
c2 = datetime.datetime.strptime('Sun 10 May 2015 13:54:36 -0000', '%a %d %B %Y %H:%M:%S %z')
print(c2)


z = (c1-c2).total_seconds()
print(type(z))
print(str(abs(int(z))))