# importing copy module
import copy
 
# initializing list 1
li1 = [1, 2, [3, 5], 4]
 
# using copy for shallow copy
li2 = copy.copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)
# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)
print("li1 ID: ", id(li1), "Value: ", li1)
li4=li1
print("li4 ID: ", id(li4), "Value: ", li4)
