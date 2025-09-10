def is_balanced(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        else:
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
                continue
    if not stack:
        return 'YES'
    else:
        return 'NO'
    
s=input()
print(is_balanced(s))