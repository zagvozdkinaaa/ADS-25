n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def count_in_range(l, r):
    if l > r:
        return 0
    return upper_bound(a, r) - lower_bound(a, l)

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    c1 = count_in_range(l1, r1)
    c2 = count_in_range(l2, r2)
    li = max(l1, l2)
    ri = min(r1, r2)
    ci = count_in_range(li, ri)
    print(c1 + c2 - ci)

