import numpy as np
#copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
#view

arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.view()
arr[0] = 42

print(arr1)
print(x)
# view & base
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#array shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
# another one
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

# reshape
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr3= arr3.reshape(4, 3)

print(newarr3)

# array iteration
arr = np.array([1, 2, 3])
# eacch element 3d dimensions
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
