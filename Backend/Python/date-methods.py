# Import the datetime package
from datetime import datetime

# Current Date and Time - now()
print(f"Current Date & Time: {datetime.now()}")

# Current Date - today()
print(f"Current Date: {datetime.today()}")

# UTC Time - utcnow()
print(f"UTC Date and Time: {datetime.utcnow()}")

# Initializing the date - datetime(year, month, day, hours, minutes, seconds)
dob = datetime(2001, 5, 15, 15, 35, 24)
print(f"I was born on {dob}")

# strftime - We can format the dates in different way or in human readable format
# %A - Day in  words full form (Monday)
# %a - Day in words short form (Mon)
# %d - Day in numerical form (15)
# %B - Month in words full form (March)
# %b - Month in words short form (Mar)
# %m - Month in numerical form (3)
# %Y - Year in numerical long form (2026)
# %y - Year in numerical short form (26)
# %H - Hour in numerical 24Hr format (15 for 3:00 PM)
# %I - Hour in numerical 12Hr format (3 for 3:00 PM)
# %p - AM & PM
# %M - Minutes
# %S - Seconds
# %f - Micro Seconds
# %Z - Timezone
# %j - Day Number out of 366 days
# %U - Week Number of year, considering Sunday as first day of week
# %W - Week Number of year, considering Monday as first day of week

# dob = datetime(2001, 1, 15, 15, 35, 24)

print(f"Birth Month: {dob.strftime("%B")}")
print(f"Birth Month - short form: {dob.strftime("%b")}")
print(f"Birth Day: {dob.strftime("%A")}")
print(f"Birth Day - short form: {dob.strftime("%a")}")
print(f"Birth Date: {dob.strftime("%d")}")
print(f"Birth Year: {dob.strftime("%Y")}")
print(f"Birth Year - short form: {dob.strftime("%y")}")
print(f"Birth Time - in Hours(24Hr): {dob.strftime("%H")}")
print(f"Birth Time - in Hours(12Hr): {dob.strftime("%I")}")
print(f"Birth Time - in Hours(12Hr): {dob.strftime("%I %p")}")

print(f"My Birthday (V1): {dob.strftime("%d %B %Y")}")
print(f"My Birthday (V2): {dob.strftime("%d %b %Y")}")
print(f"My Birthday (V3): {dob.strftime("%d %b %Y, %A")}")
print(f"My Birthday (V4): {dob.strftime("%d-%m-%Y or %d/%m/%Y or %d/%m/%y")}")

today = datetime.now()

# Month: 1 to 12 (not 01 to 12), Day: 1 to 31 (not 01 to 31)
print(f"Today is {today.strftime("%A")}")
print(f"Today is {today.strftime("%j")} day of year")
print(f"Current week is {today.strftime("%U")} week of year")

# Date Calculation
from datetime import datetime, timedelta, date

dateLimit = timedelta(weeks=1, days=5, hours=2, minutes=25)

print(f"Yesterday was {today + timedelta(days=-1)}")
print(f"Today is {today}")
print(f"Tomorrow will be {today + timedelta(days=1)}")
print(f"Date limit from today will be {today + dateLimit}")

myAge = today - dob
print(f"My age: {myAge}")