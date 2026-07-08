from numpy import *
#arr = array([10, 20, 30, 40, 50])
#print(arr)
#print(arr)
#arr= array(['Delhi', 'Hyderabad', 'Mumbai', 'Ahmedabad'], dtype=str)
#print(arr)

#Linspace Function
'''
a = linspace(0, 10, 5)
print('a = ', a)
'''
#Logspace function
'''
b = logspace(1, 4, 5)
n = len(b)
for i in range(n):
    print('%.1f'%b[i], end=' ')
'''
#Arange Function
#a = arange(2, 11, 2)
#print(a)

#Creating an array using zeros and ones function
'''
a = zeros(5, int)
print(a)
b = ones(5, int)
print(b)
'''
arr = array([10, 20, 30.5, -40])
arr = arr+5
print(arr)