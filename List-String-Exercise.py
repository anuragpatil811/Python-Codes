#create a list of 25 numeric elements and then print cube of elements which are divisible by both 3 and 5
'''
a  = []
for i in range(1, 26):
    a.append(i)
    print(a)
for i in a:
    if i%3==0 and i%5==0:
        print(i**3)
'''  
#           OR
'''
e = list(range(4, 29))
len(e)
for num in e:
    if num % 3==0 and num%5==0:
        print(num**3)
'''
#W = "Virat is top performer". Count how many words are there in the string
W = "Virat is top performer"
#print(len(W.split()))

#S = "Power BI". Make it microsoft Power BI
'''
S = "Power BI"
S = "Microsoft" + S
print(S)
'''
'''
S = "Power BI"
S.replace("Power", "Microsoft Power")
print(S)
'''
#Write a loop which will run until the value of a = 0 becomes multiple of 3 and in each iteration add 8 in the a 
a = 0
while True:
    a = a + 8
    if a%3==0:
        break
    

