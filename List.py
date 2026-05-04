W = [12, 34, 45, 56, 56, 'virat']
#Display r from the string virat
#print(W[-1][-3])
#Display the values present on even indexes
#print(W[0: :2])
#print(W[-2: :-1])

x = [12, 34, 45, 56]
#x.append(1000)
#print(x.insert(3, 2000))
#print(x.extend((3000, 4000, 5000)))
#print(x)

a = [12, 13, 14, 15, 16, 17]
#Print only emlements at even index
#print(a[0: 5: 2])
#Add 2000 at third index
#a.insert(3, 2000)
#print(a)
#Add one tuple of any 4 odd numbers in the list at last
#a.extend((3, 5, 11, 13))
#print(a)

temp = [23, 45, 12, 56, 25, 39]
#swap the positions of min temp and max temp with min temp
#print("Before Swapping:", temp)
min_temp = min(temp)
min_temp_index = temp.index(min_temp)
max_temp = max(temp)
max_temp_index = temp.index(max_temp)
temp[min_temp_index] = max_temp
temp[max_temp_index] = min_temp
#print("After Swapping:", temp)

'''
def flatten_and_sum(data):
    total = 0
    for sublist in data:
        for item in sublist:
            total += int(item)
    return total


# Example
# print(flatten_and_sum([[1, 2], [3, 4], [5]]))
'''
'''
for _ in range(int(input())):
        name = input()
        score = float(input())
        st = []
        for i in st:
            sc = []
            for j in sc:
                j.append(name)
                j.append(score)
            i.append(sc)
print(st)
'''
