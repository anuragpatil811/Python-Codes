#Program to access each element of a string in forward and reverse orders using while loop 
str = 'Core Python'
n = len(str)
i=0
while i<n:
    print(str[i], end=' ')
    i+= 1
print()
i=-1
while i>=-n:
    print(str[i], end=' ')
    i-=1
print()

