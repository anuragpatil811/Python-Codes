x, n = [int(i)   for i in input("Enter angle value, number of iterations:").split(',')]
r = (x*3.14159)/180
t = 1
sum = 1
print('Iterations=%d\t Sum=%f'%(1, sum))
i=1
for j in range(2, n+1):
    t=(-1)*t*r**2/(i*(i+1))
    sum=sum+t
    print('Iteration=%d\tSum=%f'%(j, sum))
    i += 2