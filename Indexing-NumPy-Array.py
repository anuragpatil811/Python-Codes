from numpy import *
a = arange(10, 16)
print("Original Array:", a)
#retrieve from 1st to one element prior to 6th element in steps of 2
a = a[1:6:2]
print(a)
i=0
while (i<len(a)):
    print(a[i])
    i += 1