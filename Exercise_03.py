#Q1) WAP: to check password validity, length between 8 to 16, atleast one capital letter, atleast one small letter, atleast one special symbol
"""""
print("Password Must contain atleast one small letter, one capital letter", "Password length is 8 to 16 digit", "atleast one special character @#$")
password = input("Enter your password:")
import re
x = True
while x:
    if len(password)<8 or len(password) > 16:
        break
    elif not re.search("[A-Z]", password):
        break
    elif  not re.search("[a-z]", password):
        break
    elif not re.search("[@#S]", password):
        break
    else:
        print("Password is a valid password")
        x = False
        break

if x:
    print("Password is invalid")
"""""
#Q2) WAP: to get country code using phone numbers
"""""
import re
numbers = ["+91-9420667071", "+1-9420667072", "+22-8999041253"]
def callingcode(number):
    pattern = r'(\+\d+)-'
    for number in numbers:
        match = re.findall(pattern, number)
        if match:
            print(f"{number} Country Code is {match}")
callingcode(numbers)
"""
#Q3) WAP: Sum  of list using Recursion
"""
size = int(input("Enter size of list:"))
list = []
for i in range(size):
    temp = int(input(f"Enter {i} index value"))
    list.append(temp)
print(list)

def listsum(list):
    if not list:
        return 0
    else:
        return list[0] + listsum(list[1:])
print(listsum(list))
"""
#Q4) WAP: to get last term of Fibonnacci Series using Recursion
num = int(input("Enter the index of Fibonnacci Series:"))
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(num))