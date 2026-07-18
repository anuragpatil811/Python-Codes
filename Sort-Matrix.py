from numpy import *
m = matrix([[5, 4, 1], [2, 7, 0]])
print(m)
a = sort(m)
print("Sorted rows:", a)
b = sort(m, axis=0)
print("Sorted columns:", b)