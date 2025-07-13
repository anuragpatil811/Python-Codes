#Q.1) WAP: to calculate Quadratic Roots
#Quadratic equation: "ax2 + bx + c = 0"
"""""
import math
def quadratic(a, b, c):
    if a == 0:
        print("Not a Quadratic Equation")
    else: 
        discriminant = b**2 - 4*a*c
    print(discriminant)
    if discriminant < 0:
        print("No real roots Imaginary roots")
    elif discriminant == 0:
        root = -b/2+a
        print(f"Two roots present {positiveroot} and - {negativeroot}")
    else:
        positiveroot = (-b + math.sqrt(discriminant)) / 2 * a
        negativeroot = (-b - math.sqrt(discriminant)) / 2 * a
        print(f"Only one root present {root}")
a = float(input("Enter value of coefficient of x2:"))
b = float(input("Enter value of coefficient of x:"))
c = float(input("Enter value of constant:"))
quadratic(a, b, c)"
"""
#Q.2) WAP: to calculate Sine, Cosine, Tangential
"""""
import math
def trigonometry(degree):
    rad = math.radians(degree)
    sine = math.sin(rad)
    cosine = math.cos(rad)
    tan = math.tan(rad)
    print(f"Sine{degree}:{sine}")
    print(f"cosine{degree}:{cosine}")
    print(f"Tan{degree}: {tan}")
    #print(sine)
    #print(cosine)
degree = int(input("Enter your degree:"))
trigonometry(degree)"
"""
#Q.3) WAP: to generate OTP/Capcha
"""""
import random
import string
def randomotp(length):
    letters = string.digits 
    temp = []
    for i in range(length):
        x = random.choice(letters)
        temp.append(x)
    return "".join(temp)
        #otp = "".join(temp)
length = int(input("Enter length of OTP:"))
otp = randomotp(length)
print(f"Your random Capcha is {otp}")"
"""
#Q.4) WAP: Random Password Generation
import random
import string
length = 16
def randompassword(length):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation
    password = [random.choice(upper), 
                random.choice(lower),
                random.choice(numbers),
                random.choice(special)]
    allcharacters = upper + lower + numbers + special
    #print(allcharacters)
    for i in range(length - len(password)):
        temp = random.choice(allcharacters)
        password.append(temp)
    random.shuffle(password)
    password_str = "".join(password)
    print(f"Random Password using Random Module: {password_str}")
randompassword(length)