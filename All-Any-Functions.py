from numpy import *
a = array([1, 2, 3, 0])
b = array([0, 2, 3, 1])
c = a > b
print('Result of a>b:', c)
print('Check if all elements are true:', all(c))
print('Check if any elements are true:', any(c))
if (any(a>b)):
    print('a contains atleast one element greater than those of b')