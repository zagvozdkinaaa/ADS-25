#density of mixtures must be >=m
#find num of operations
import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr)

ops=0

while arr and arr[0] < m:
    if len(arr) < 2:
        print(-1)
        break
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    new = a+2*b
    heapq.heappush(arr, new)
    ops+=1
else:
    print(ops)