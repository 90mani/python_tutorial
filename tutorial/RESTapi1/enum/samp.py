
from enum import Enum

class month(Enum):
	JANUARY = 1
	FEBRUARY = 2
	MARCH = 3
	APRIL = 4

# printing enum member as string
print(month.JANUARY)

# printing name of enum member using "name" keyword
print(month.JANUARY.name)

# printing value of enum member using "value" keyword
print(month.JANUARY.value)

# printing the type of enum member using type()
print(type(month.JANUARY))

# printing enum member as repr
print(repr(month.JANUARY))

# printing all enum member using "list" keyword
print(list(month))
