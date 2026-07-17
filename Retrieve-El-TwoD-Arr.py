#Program to retrieve the elements from a 2 D array and display them using for loops 
from numpy import *
a = [[1, 2, 3], [4,5,6], [7, 8, 9]]
for i in range(len(a)):
    print(a[i])
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])