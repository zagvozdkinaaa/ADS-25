
n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

min_length = n + 1

for left in range(n):
    if prefix[n] - prefix[left] < k:
        continue


    low = left + 1
    high = n
    best_right = n

    while low <= high:
        mid = (low + high) // 2
        current_sum = prefix[mid] - prefix[left]

        if current_sum >= k:
            best_right = mid
            high = mid - 1  
        else:
            low = mid + 1 

    length = best_right - left
    if length < min_length:
        min_length = length

print(min_length)
