x, n = [int(i) for i in input("Enter power of e, number of iterations:").split(',')]
t=1
sum=t
print('Iteration=%d\t Sum=%f'%(1, sum))
for j in range(1, n):
    t = t*x/j
    sum=sum+t
    print('Iteration=%d\t Sum=%f'%(j+1, sum))