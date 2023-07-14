from pickle import TRUE


def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
            return False
    if year % 100 == 0:
            return False
    else:
            return True

    if year % 400 == 0:
             return True
    else:
            return False

# Test the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
