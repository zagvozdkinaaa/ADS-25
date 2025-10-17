n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(m)]
b_with_index = sorted([(val, i) for i, val in enumerate(b)])

res = [0] * m
current_line = 0
block = 1
idx = 0

for lines in a:
    current_line += lines
    while idx < m and b_with_index[idx][0] <= current_line:
        res[b_with_index[idx][1]] = block
        idx += 1
    block += 1

print('\n'.join(map(str, res)))

