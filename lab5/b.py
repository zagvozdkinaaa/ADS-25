#choose the two heaviest rocks and smash
#find weight of the last stone 

import heapq

n = int(input())
stones = list(map(int, input().split()))

stones = [-x for x in stones]
heapq.heapify(stones)

while len(stones) > 1:
    y = -heapq.heappop(stones)
    x = -heapq.heappop(stones)
    if y!=x:
        heapq.heappush(stones, -(y-x))

print(-stones[0] if stones else 0)