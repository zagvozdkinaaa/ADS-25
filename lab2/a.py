n = int(input())
arr = list(map(int, input().split()))
k = int(input())

min_dist = abs(arr[0]-k)
index = 0

for i, num in enumerate(arr):
    dist = abs(num-k)
    if dist < min_dist:
        min_dist = dist
        index = i

print(index)