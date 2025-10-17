
n, k = map(int, input().split())
a = list(map(int, input().split()))

left, right = max(a), sum(a)

while left < right:
    mid = (left + right) // 2
    blocks, current_sum = 1, 0

    for ghouls in a:
        if current_sum + ghouls > mid:
            blocks += 1
            current_sum = ghouls
        else:
            current_sum += ghouls

    if blocks <= k:  
        right = mid
    else:            
        left = mid + 1

print(left)
