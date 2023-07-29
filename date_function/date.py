import datetime
tdate=datetime.date(1999,5,31)
print("Date format:",tdate)

tdate=datetime.date.today()
print("Today date:",tdate)

print("year:",tdate.year)
print("month:",tdate.month)
print("day:",tdate.day)



      

wday =tdate.weekday()
print("weekday:",wday)


isowday=tdate.isoweekday()
print("ISO Weekday:",isowday)

timedelta=datetime.timedelta(days=3)
print("Time Delta:",tdate+timedelta)

newyear=datetime.date(2023,3,20)
daypass=tdate-newyear
print("No of days passed:",daypass.days)

ttime=datetime.time(8,30,45)
print("Time:",ttime)

hours=ttime.hour
print("Hours:",hours)

minutes=ttime.minute
print("Minutes:",minutes)

sec=ttime.second
print("second:",sec)
