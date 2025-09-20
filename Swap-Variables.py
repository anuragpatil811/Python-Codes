a = 5
b = 10
"""""
a, b = b, a
print(a, b)
"""
temp = a
a = b
b = temp
print(a, b)