#Program to accept a matrix from the keyboard and display its transpose matrix.
from numpy import * 
r, c  = [int(a)  for a in input("Enter rows, columns:").split()]
str = input("Enter matrix elements:")
x = reshape(matrix(str), (r, c))
print("Original Array:", x)
y = x.transpose()
print("Transposed Matrix:", y)