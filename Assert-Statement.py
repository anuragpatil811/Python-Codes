'''
x = int(input("Enter a number greater than zero:"))
assert x > 0, "Wrong input entered"
print(x)
'''

x = int(input("Enter a number greater than 0:"))
try:
    assert(x>0)
    print("You entered:", x)
except AssertionError: 
    print("Wrong input entered")