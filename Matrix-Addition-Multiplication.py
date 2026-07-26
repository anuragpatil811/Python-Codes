from numpy import * 
a = matrix('1 2 3; 4  5  6')
b = matrix('2 2 2; 1 -1 2')
print(a)
print(b)
c = a+b
print("Addition:", c)
d = a/b
print("Division:", d)
e = a*b
print("Mutiplication:", e)