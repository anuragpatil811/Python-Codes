a = ['Zomato', 'Zepto', 'Lenskart', 'Paytm']
#print(a[0:3])
#Write a loop to print every second character in capital order
'''
for i in a:
   print(i[1].upper())
''' 

q = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#Create a list of every day without day in it e.g. ['Mon', 'Tues'...]
'''
for i in q:
   print(i.replace('day', ''))
'''
#Method 2
'''
days_without_day = []
for day in q:
   days_without_day.append(day[0:3])  
   print(days_without_day)
'''

a = [12, 23, 34, 45, 56, 67]
#Change the code as if the number is odd but divisible by 5 then append the cube of that number
'''
square_list = []
for i in a:
    if i%2 == 0:
        square_list.append(i**2)
#    elif i%5==0:
#        square_list.append(i**3)
    else: 
        if i%5==0:
           square_list.append(i**3)
        else:
          square_list.append(i)
print(square_list)
'''
