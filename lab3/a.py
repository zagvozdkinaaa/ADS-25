t = int(input())
targets=list(map(int, input().split()))
n, m = map(int, input().split())

positions = {}

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        positions[row[j]]=(i,j)

for x in targets:
    if x in positions:
        print(positions[x][0], positions[x][1])
    else:
        print(-1)