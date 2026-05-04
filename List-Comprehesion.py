q = [1, 2, 3, 4]
x = [i**2  for i in q  if i%2==1]
#print(x)

#Create a list of numbers which are divisible by 3 and 5
q = [12, 23, 45, 56, 67, 89, 90, 54]
a = [i   for i in q   if i%3==0 and i%5==0]
#print(a)
#Create a list of tuples containing square and cube of both the odd number in q
q = [12, 23, 45, 56, 67, 89, 90, 54]
b = [(i**2, i**3)  for i in q  if i%2==1]
#print(b)

#Create a tuple comprehension of len's of all names from 
t = ('Virat', 'dhoni', 'sachin', 'arjum')
lengths = tuple([len(i)  for i in t ])
#print(lengths)

#Create the following output using list comprehesion
#Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
d = [[0, 0, 0] for i in range(3)]
#print(d)
#                   OR
e = [[0 for j in range(3)]  for i in range(3)]   #nested list comprehesion
#print(e)

#Redesign the following code using list comprehension
'''
F = [12, 23, 34, 123, 33, 56]
E = []
for i in F:
    if i%2==0:
        E.append(i**2)
    elif i%3==0:
        E.append(i)
    else:
        E.append(i**3)
'''
'''
F = [12, 23, 34, 123, 33, 56]
E = []
sample = [i**2 if i%2==0 else i if i%3==0 else i**3 for i in F]
print(sample)
'''
#Write a list comprehension code to get the following output: [[[1, 2, 3]]]
q = [[[1, 2, 3]] for i in range(1) ]
print(q)

W = [12, 23, 45, 56, 67, 67, 78]
#write a list comprehesion to create a lists of square of number divisible by 4, cube of num divisible by 5 and multiply by
# the same num which is divisible by 3 if above conditions does not satisfy. If no condition satisfy then add num as it is
r = [i**2 if i%4==0 else i**3 if i%5==0 else i**i if i%3==0 else i for i in W]
print(r)