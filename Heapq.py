import heapq
heap = []
#Heappush function
heapq.heappush(heap, 10)
#print(heap)
heapq.heappush(heap, 1)
#print(heap)
heapq.heappush(heap, 5)
#print(heap)  

#Heappop function
heapq.heappop(heap)
heapq.heappop(heap)
#print(heap)

#Heapify function
list1 = [1, 3, 5, 2, 4, 6]
heapq.heapify(list1)
#print(list1)

#Heappushpop function
heapq.heappushpop(list1, 89)
#print(list1)

#Heapreplace function
heapq.heapreplace(list1, 100)
#print(list1)

#nsmallest function
heapq.nsmallest(2, heap)
#print(heap)

#nlargest function
print(heapq.nlargest(3, heap))

