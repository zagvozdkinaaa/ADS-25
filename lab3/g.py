n, f = map(int, input().split())
kids = list(map(int, input().split()))

left=1
right=max(kids)
answer = right

while left <= right:
    mid = (left+right)//2
    total = 0
    for x in kids:
        total += (x+mid-1)//mid
        if total > f:
            break

    if total <= f:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)