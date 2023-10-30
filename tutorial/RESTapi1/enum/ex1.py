from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

# Accessing enum member using value
print("The enum member associated with value 2 is : ", Season(2).name)

# Accessing enum member using name
print("The enum member associated with name AUTUMN is : ", Season['AUTUMN'].value)
