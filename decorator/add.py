def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_50 = create_adder(50)
 
print(add_50(10))
