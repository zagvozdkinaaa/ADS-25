def solve():
    n = int(input())
    ages = list(map(int, input().split()))

    stack = []
    result = []

    for i in range(n):
        while stack and stack[-1] > ages[i]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(ages[i])

    print(' '.join(map(str, result)))

solve()