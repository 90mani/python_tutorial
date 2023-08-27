def shout(text):
    return text.upper()
 
def fun(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am ready to work.""")
    print (greeting)
 
greet(shout)
greet(fun)
