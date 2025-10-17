n, k = map(int, input().split())
sheep = [tuple(map(int, input().split())) for i in range(n)]

limits = [max(x2, y2) for x1, y1, x2, y2 in sheep]

left, right = 1, 10**9
answer = right

while left <= right:
    mid = (left+right)//2
    count = 0

    for val in limits:
        if val <= mid:
            count += 1
        
    if count >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)