from collections import deque

n = int(input())
st = input()

s = deque()
k = deque()

for i, ch in enumerate(st):
    if ch == 'S':
        s.append(i)
    else:
        k.append(i)

while s and k:
    s_i = s.popleft()
    k_i = k.popleft()

    if s_i < k_i:
        s.append(s_i+n)
    else:
        k.append(k_i+n)
    
if s:
    print('SAKAYANAGI')
else:
    print('KATSURAGI')