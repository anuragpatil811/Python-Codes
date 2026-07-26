#Python program to find the first occurence of sub string in a given string using index() method
str = input("Enter main string:")
sub = input("Enter sub string")
try:
    n = str.index(sub, 0, len(str))
except ValueError:
    print('Sub string not found')
else:
    print('Sub string found at position:', n+1)