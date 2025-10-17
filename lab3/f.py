n = int(input())
a = list(map(int, input().split()))
p = int(input())
powers = [int(input()) for i in range(p)]

a.sort()

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]

for power in powers:
    left, right = 0, len(a)
    while left < right:
        mid = (left+right)//2
        if a[mid] <= power:
            left = mid + 1
        else:
            right = mid
    idx = left 
    count = idx
    total = prefix[idx]
    print(count, total)