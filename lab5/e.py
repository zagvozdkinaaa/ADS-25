#can store only k boxes with cookies
#max sum of cookies after being given a box of n cookies
import heapq

q, k = map(int, input().split())
heap = []
total_sum = 0

for i in range(q):
    command = input().split()
    if command[0] == "insert":
        n = int(command[1])
        if len(heap) < k:
            heapq.heappush(heap, n)
            total_sum += n
        elif n > heap[0]:
            total_sum -= heapq.heappop(heap)
            heapq.heappush(heap, n)
            total_sum += n
    else:
        print(total_sum)
