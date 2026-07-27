#Program to search for the position of a string in a given group of strings
str = []
n = int(input("How many strings?:"))
for i in range(n):
    print("Enter strings:")
    str.append(input())
s = input("Enter target string:")
flag = False
for i in range(len(str)):
    if s==str[i]:
        print("Found at ", i+1)
        flag=True
if flag==False:
    print("Not found")