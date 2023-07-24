#Map is a function executes a specified function for each item in an iterable.
#The item is send to the functions as a parameters
#easy to type as one line coding



#adding 1+1 functions

def myfunc(a,b):
    return a+b
x=list(map(myfunc,('abble','banana','cherry'),('orange','leamon','pineapple')))

print(x)


#squre the given value useing map function 

def squre (a):
    return a*a

num=[1,2,3,4,5,6,7,8,9,10]

print(num)

num=list(map(squre,num))

print(num)
