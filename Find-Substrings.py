str = input("Enter main string:")
sub = input("Enter sub string:")
n = str.find(sub, 0, len(str))
if n== -1:
    print('Sub string not found')
else:
    print("Sub string found at position:", n+1)