def solve(s):
    stack = []

    for ch in s:
        if ch == '#' and stack:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

s1, s2 = input().split()

if solve(s1) == solve(s2):
    print('Yes')
else:
    print('No')