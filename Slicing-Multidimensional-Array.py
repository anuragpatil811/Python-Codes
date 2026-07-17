from numpy import *
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = reshape(a, (3, 3))
#Display 0th row
print(a[0, :])
#Display 0th column 
print(a[:, 0])
#Retrieve 0th row and 0th column
print(a[0:1, 0:1])
#Retrieve 1st row and second column
print(a[1:2, 1:2])
#Retrieve 2nd row and 2nd column element 
print(a[2:3, 1:2])


b = reshape(arange(11, 36, 1), (5, 5))
print(b)
#Display top 2 rows and 3 columns 
print(b[0:2, 0:3])
#Display 2nd row to third row, 3rd column to last column
print(b[2:4, 3:])
#To access the lower right 3 rows and 2 columns, we can write
print(b[2:, 3:])