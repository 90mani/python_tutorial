from enum import Enum
 
class Weekdays(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY= 4
 
# Accessing enum member using value
print("The enum member associated with value 2 is : ", Weekdays(2).name)

# Accessing enum member using name
print("The enum member associated with name MONDAY is : ", Weekdays['MONDAY'].value)
