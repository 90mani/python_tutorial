from enum import Enum
 
class Weekdays(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY= 4
 
# printing enum member as string
print(Weekdays.SUNDAY)
 
# printing name of enum member using "name" keyword
print(Weekdays.SUNDAY.name)
 
# printing value of enum member using "value" keyword
print(Weekdays.SUNDAY.value)
 
# printing the type of enum member using type()
print(type(Weekdays.SUNDAY))
 
# printing enum member as repr
print(repr(Weekdays.SUNDAY))
 
# printing all enum member using "list" keyword
print(list(Weekdays))
