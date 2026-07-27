#Program to know the type of character entered by the user
str = input("Enter a character:")
ch = str[0]
if ch.isalnum():
    print("It is alphabet or numeric character")
    if ch.isalpha():
        print("It is an alphabet")
        if ch.isupper():
            print("It is capital letter")
        else:
            print('It is lowercase letter')
    else:
        print("It is numeric digit")
elif ch.isspace():
    print("It is a space")
else:
    print('It may be a special character')
