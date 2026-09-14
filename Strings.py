str1 = 'Anurag'
#print(str1[-4])

w = 'virat is good cricketer'
#print(w[2: 5])
#print(w[2:-18])
#print(w[-21: -18])
#print(w[-21: 5])

e = 'this is data science, I am learning ML'
#Retrieve data science
#print(e[8:20])

#Retrieve Data science in reverse order
#print(e[19: 7: -1])

#Retrieve ML in reverse order
#print(e[-1:-3:-1])

#From Right to Left print every second character
#print(e[-1: : -2])

#**Create a string a='virat is a good cricketer' **
#print this string in reverse order
a = 'virat is a good cricketer'
#print(a[::-1])

#print only those characters which are at odd index
#print(a[1:24:2])

#Write a function which will print +ve as well as -ve index of each character in the inputed string
def indx(s):
  n = len(s)
  for i, ch in enumerate(s):
    print(i, ch, i-n)   
s = input("Enter a string:")
indx(s)