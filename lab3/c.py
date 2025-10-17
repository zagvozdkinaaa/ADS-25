n, q = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    count = 0
    for x in a:
        if (l1 <= x <= r1) or (l2 <= x <= r2):
            count+=1

    print(count)