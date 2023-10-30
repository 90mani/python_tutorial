import enum

# creating enumerations using class
class Animal(enum.Enum):
	dog = 1
	cat = 2
	lion = 3

# Hashing enum member as dictionary
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

# checking if enum values are hashed successfully
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
	print("Enum is hashed")
else:
	print("Enum is not hashed")
