#Use where function to compare two arrays and return the maximum value of each element
from numpy import *
a = array([10, 20, 30, 40, 50], int)
b = array([1, 21, 3, 40, 51], int)
c = where(a>b, a, b)
print(c)