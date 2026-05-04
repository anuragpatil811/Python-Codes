'''
n = Total number of elements
**For Odd elements**
----> (n+1)/2 -1
**For Even elements
----> (n/2) - 1 + (n/2)
'''
F = [12, 234, 45, 23, 57, 78, 23]
#Print the median of the above list

#median = (s[3] + s[4]) / 2
#print(median)
if len(F)%2==1:
    sorted_list = sorted(F)
    n = len(F)
    median = F[(n+1)//2 - 1]
    print(median)
else:
     sorted_list = sorted(F)
     n = len(F)
     first_mid = F[n//2 - 1]
     second_mid = F[n//2]
     median = (first_mid + second_mid)/2
     print(median)