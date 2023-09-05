def my_generator(n):
    #initialize counter
    value =0
    #loop until counter is less then n
    while value < n:
        #produce the current value of the counter
        yield value
        #increment the counter
        value += 1
#print each value produced by generator object produced by my_generator
for value in my_generator(3):
    #print each value produced by generator
    print(value)        

