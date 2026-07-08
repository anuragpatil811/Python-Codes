from numpy import * 
a = arange(1, 6)
b = a 
print('Original Array:', a)
print('Alias Array:', b)
b[0] = 99
print("After Modification:")
print("Original Array:", a)
print("Alias Array:", b)