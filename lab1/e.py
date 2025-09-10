from collections import deque

boris_cards = deque(map(int, input().split()))
nursik_cards = deque(map(int, input().split()))

max_moves = 10**6
moves = 0

while boris_cards and nursik_cards and moves != max_moves:
    moves+=1

    b = boris_cards.popleft()
    n = nursik_cards.popleft()

    if (b == 0 and n == 9) or (b>n and not (b==9 and n==0)):
        boris_cards.append(b)
        boris_cards.append(n)
    else:
        nursik_cards.append(b)
        nursik_cards.append(n)

if moves >= max_moves:
    print("blin nichya")
elif not boris_cards:
    print("Nursik", moves)
else:
    print("Boris", moves)