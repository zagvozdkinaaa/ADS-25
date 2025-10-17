#price = vacant seats
#the maximum amount of money the stadium can earn
import heapq

n, x = map(int, input().split())
a = list(map(int, input().split()))

heap = [-val for val in a if val > 0]
heapq.heapify(heap)

total = 0

for i in range(x):
    k = -heapq.heappop(heap)
    total += k
    
    if k-1>0:
        heapq.heappush(heap, -(k-1))

print(total)