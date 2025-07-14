def sq(n):
    i = 1
    lst = []
    while i<=n:
        yield i*i
       # lst.append(n*n)
        i += 1
   # return lst
temp = sq(10)
print(temp.__next__())
print(temp.__next__())
print(temp.__next__())