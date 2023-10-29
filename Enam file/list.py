from enum import Enum
 
class Weekdays(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY= 4
 
 
for Weekdays in (Weekdays):
    print(Weekdays.value,"-",Weekdays)
