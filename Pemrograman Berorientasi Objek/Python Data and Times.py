# pylint: disable=reimported

#Python datetime
#Example 1: Get Current Date and Time
import datetime

# get the current date and time
now = datetime.datetime.now()

print(now)

#Example 2: Get Current Date
import datetime

# get current date
current_date = datetime.date.today()

print(current_date)

#Attributes of datetime Module
import datetime

print(dir(datetime))

#Python datetime.date Class
#Example 3: Date object to represent a date
import datetime

d = datetime.date(2022, 12, 25)
print(d)

#Import Only date Class
from datetime import date

d = date(2022, 12, 25)
print(d)

#Example 4: Get the current date using today()
from datetime import date

# today() to get current date
todays_date = date.today()

print("Today's date =", todays_date)

#Example 5: Get the date from a timestamp
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

#Example 6: Print today's year, month and day
from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Python datetime.time Class
#Example 7: Time object to represent time
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)

#Example 8: Print hour, minute, second and microsecond
from datetime import time

a = time(11, 34, 56)

print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

#The datetime.datetime Class
#Example 9: Python datetime object
from datetime import datetime

# datetime(year, month, day)
a = datetime(2022, 12, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)

#Example 10: Print year, month, hour, minute and timestamp
from datetime import datetime

a = datetime(2022, 12, 28, 23, 55, 59, 342380)

print("Year =", a.year)
print("Month =", a.month)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Timestamp =", a.timestamp())

#Python datetime.timedelta Class
#Difference between two dates and times
from datetime import datetime, date

# using date()
t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)

t3 = t1 - t2

print("t3 =", t3)

# using datetime()
t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t4 - t5
print("t6 =", t6)

print("Type of t3 =", type(t3))
print("Type of t6 =", type(t6))

#Example 12: Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)

t3 = t1 - t2

print("t3 =", t3)

#Example 14: Time duration in seconds
from datetime import timedelta

t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("Total seconds =", t.total_seconds())

#Python strftime() Method
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

#Python strptime() Method
from datetime import datetime

date_string = "25 December, 2022"
print("date_string =", date_string)

# use strptime() to create date object
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)

#Handling timezone in Python
from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

#Python strftime()
#Example 1: Datetime to string using strftime()
from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

#Example 2: Creating string from a timestamp
from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)

#Example 3: Locale's appropriate date and time
from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%c")
print("Output 1:", d)

d = date_time.strftime("%x")
print("Output 2:", d)

d = date_time.strftime("%X")
print("Output 3:", d)

#Python strptime()
#Example 1: String to datetime object
from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

#Example 2: String to datetime object with two formats
from datetime import datetime

dt_string = "12/11/2018 09:15:32"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

#Python Get Current Date and Time
#Example 1: Get today's date
from datetime import date

today = date.today()
print("Today's date:", today)

#Example 2: Current date in different formats
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

#Example 3: Get the current date and time in Python
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

#Python Get Current Time
#Example 1: Current time using datetime object
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#Example 2: Current time using time module
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#Example 3: Current time of a certain timezone
from datetime import datetime
import pytz

# Get the timezone object for New York
tz_NY = pytz.timezone('America/New_York')

# Get the current time in New York
datetime_NY = datetime.now(tz_NY)

# Format the time as a string and print it
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

# Get the timezone object for London
tz_London = pytz.timezone('Europe/London')

# Get the current time in London
datetime_London = datetime.now(tz_London)

# Format the time as a string and print it
print("London time:", datetime_London.strftime("%H:%M:%S"))

#Python Timestamp to datetime and Vice Versa
#Example 1: Python timestamp to datetime
from datetime import datetime

# timestamp is number of seconds since 1970-01-01
timestamp = 1545730073

# convert the timestamp to a datetime object in the local timezone
dt_object = datetime.fromtimestamp(timestamp)

# print the datetime object and its type
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

#Example 2: Python datetime to timestamp
from datetime import datetime

# current date and time
now = datetime.now()

# convert from datetime to timestamp
ts = datetime.timestamp(now)

print("Timestamp =", ts)

#Python time Module
#Example 1: time.time() Function
import time

# get the current time in seconds since the epoch
seconds = time.time()

print("Seconds since epoch =", seconds)

#Example 2: time.ctime() Function
import time

# seconds passed since epoch
seconds = 1672215379.5045543

# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)

print("Local time:", local_time)

#Example 3: time.sleep() Function
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

#Example 4: time.localtime() Function
import time

result = time.localtime(1672214933)

print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

#Example 5: time.gmtime() Function
import time

result = time.gmtime(1672214933)

print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

#Example 6: time.mktime() Function
import time

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

# convert time_tuple to seconds since epoch
seconds = time.mktime(time_tuple)

print(seconds)

#Example 7: time.asctime() Function
import time

# time tuple
t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

#Example 8: time.strftime() Function
import time

# current date and time
named_tuple = time.localtime()

# format time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)

#Example 9: time.strptime() Function
import time

# time string
time_string = "14 July, 2023"

# parse time string
result = time.strptime(time_string, "%d %B, %Y")

print(result)

#Python sleep()
#Example 1: Python sleep() Example
import time

time.sleep(2)

print("Wait until 2 seconds.")

#Example 2: sleep() Method
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

#Example 3: Create a Digital Clock in Python
import time

while True:
    # get current local time as structured data
    current_time = time.localtime()

    # format the time in 12-hour clock with AM/PM
    formatted_time = time.strftime("%I:%M:%S %p", current_time)

    print(formatted_time)
    time.sleep(1)
