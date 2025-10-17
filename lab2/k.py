from collections import Counter, deque

t = int(input())

for i in range(t):
    n = int(input())
    stream = input().split()

    count = Counter()
    dq = deque()
    result = []
    
    for ch in stream:
        count[ch] += 1
        dq.append(ch)

        while dq and count[dq[0]] > 1:
            dq.popleft()

        if dq:
            result.append(dq[0])
        else:
            result.append("-1")
    
    print(" ".join(result))