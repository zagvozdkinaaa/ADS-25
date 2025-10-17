n, h = map(int, input().split())
bags = list(map(int, input().split()))

left = 1
right = max(bags)
answer = right

while left <= right:
    mid = (left + right) // 2 
    hours = 0
    for gold in bags:
        hours += (gold + mid - 1) // mid 

    if hours <= h:
        answer = mid
        right = mid - 1 
    else:
        left = mid + 1 

print(answer)
