from collections import deque

dq = deque()

while True:
    command = input().split()
    if not command:
        continue
    if command[0] == '!':
        break
    elif command[0] == '+':
        dq.appendleft(int(command[1]))
    elif command[0] == '-':
        dq.append(int(command[1]))
    elif command[0] == '*':
        if not dq:
            print('error')
        else:
            if len(dq) == 1:
                print(dq[0]+dq[0])
                dq.pop()
            else:
                print(dq[0]+dq[-1])
                dq.pop()
                dq.popleft()