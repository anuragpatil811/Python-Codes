#Program to sort a group of strings into alphabetical order
str = []
n = int(input("How many strings?"))
for i in range(n):
    print("Enter string:", end='')
    str.append(input())
str1 = sorted(str)
print("Sorted list:")
for i in str1:
    print(i)