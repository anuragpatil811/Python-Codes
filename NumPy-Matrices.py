from numpy import *
arr = [[1, 2, 3], [4, 5, 6]]
a = matrix(arr)
print(a)
str = '1 2; 3 4; 5 6'
b = matrix(str)
print(b)

#return Diagonal Elements
#c = diagonal(b)
#print(c)

c = matrix('1 2 3; 4 5 6; 7 8 9')
print(c)
d = diagonal(c)
print(d)

#Maximum and Minimum elements 
big = a.max()
print(big)
small = a.min()
print(small)

print("Sum:", a.sum())
print("Average:", a.mean())

m =  matrix(arange(12).reshape(3, 4))
print("matrix:", m)

e = m.prod(0)
print("Product of elements in 0th column:", e)

f = m.prod(1)
print("Product of row elements:", f)