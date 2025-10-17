n = int(input())
names = [input() for i in range(n)]

unique_names = []
prev = None

for name in names:
    if name != prev:
        unique_names.append(name)
    prev = name

unique_names.reverse()

print(f'All in all: {len(unique_names)}')
print('Students:')
for name in unique_names:
    print(name)