import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[2] = 46

print(arr)
print(x)
