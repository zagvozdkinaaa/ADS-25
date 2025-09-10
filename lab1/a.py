from collections import deque

def focus(n):
    dq = deque()
    for i in range(n,0,-1):
        dq.appendleft(i)
        k = i % len(dq)
        dq.rotate(k)
    return list(dq)

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    result = focus(n)
    print(' '.join(map(str,result)))
