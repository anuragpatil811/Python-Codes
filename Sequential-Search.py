from array  import *
x = array('i', [])
n = int(input("Enter the number of elements:"))
for i in range(n):
    x.append(int(input("Enter elements:")))
s = int(input("Enter the target elements:"))
flag=False
for i in range(len(x)):
    if s==x[i]:
        print('Found at Position=', i+1)
        flag=True
if flag==False:
    print("Not Found in the array")