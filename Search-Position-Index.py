from array import *
x = array('i', [])
print('How many elements?', end='')
n = int(input())
for i in range(n):
    x.append(int(input("Enter the elements:")))
print('Enter element to search:', end='')
s = int(input())
try:
    pos = x.index(s)
    print("Found at position=", pos+1)
except ValueError:
    print("Not found in the array:")