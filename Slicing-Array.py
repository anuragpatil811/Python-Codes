from numpy import *
a = arange(10, 16)
print("Original Array:", a)
b = a[1:6:2]
#print(b)

#retrieve all elements from a 
b = a[::]
#print(b)

#retrieve from 6-2=4th to one element prior to 4th element (6-2=4th)
b = a[:-2:]
print(b)