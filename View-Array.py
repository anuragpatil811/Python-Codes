from numpy import *
a = arange(1, 6)
b = a.view()
print('Original array:', a)
print('New array', b)
b[0] = 99
print("After modification:")
print("Origianl Array:", a)
print("New Array", b)