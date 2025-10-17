from collections import deque

n, k = map(int, input().split())
words = input().split()
dq = deque(words)

dq.rotate(-k)

print(' '.join(dq))