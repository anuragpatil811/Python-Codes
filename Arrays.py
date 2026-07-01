#import array 
#a = array.array('i', [5, 6, -7, 8])]
from array import *
#a = array('i', [2, 3, 4, 5])
'''
for element in a:
    print(element)
'''
'''
arr = array('u', ['a', 'b', 'c', 'd', 'e'])
print('The array elements are:')
for ch in arr:
    print(ch)
'''

#Python program to create one array from another array
'''
arr1 = array('d', [1.5, 2.5, -3.5, 4])
arr2 = array(arr1.typecode, (a*3 for a in arr1))
print('The arr2 elements are:')
for i in arr2:
    print(i)
'''
#Program to retrieve elements of an array using while loop
'''
x = array('i', [10, 20, 30, 40, 50])
n = len(x)
for i in range(n):
    print(x[i], end='')
'''
#Program to retrieve elements of an array using index
'''
x = array('i', [10, 20, 30, 40, 50])
n = len(x)
i=0
while i<n:
    print(x[i], end=' ')
    i += 1
'''
#Slicing Operations
x = array('i', [10, 20, 30, 40, 50])
print(x[1:4])
print(x[0:])
print(x[:-4])
print(x[-4:])
print(x[-4:-1])
print(x[0:7:2])