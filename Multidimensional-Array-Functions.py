from numpy import *
a = ones((3, 4), int)
print(a)
b = zeros((3, 4), float)
print(b)
 #c= reshape(a, (4, 3, 4))
#print(c)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ') 