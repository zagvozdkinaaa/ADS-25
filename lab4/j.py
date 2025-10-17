def build(arr):
    if not arr:
        return []
    mid = len(arr) // 2
    return [arr[mid]] + build(arr[:mid]) + build(arr[mid+1:])

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(*build(a))
