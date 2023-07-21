# python  map.
 
def addition(n):
    return n + n
 
# double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
