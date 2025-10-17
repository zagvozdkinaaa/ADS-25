class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert(head, x, p):
    new_node = Node(x)
    if p == 0:
        new_node.next = head
        return new_node
    current = head

    for i in range(p - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head

def remove(head, p):
    if p == 0:
        return head.next
    current = head 
    for i in range(p - 1):
        current = current.next
    current.next = current.next.next
    return head

def print_linked_list(head):
    current = head 
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    print(' '.join(result))

def replace(head, p1, p2):
    if p1 == p2:
        return head
    if p1 == 0:
        node = head
        head = head.next
    else:
        cur = head
        for i in range(p1 - 1):
            cur = cur.next
        node = cur.next
        cur.next = node.next

    if p2 == 0:
        node.next = head
        head = node

    else:
        cur = head
        for i in range(p2 - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node

    return head 

def reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def cyclic_left(head, x):
    if not head:
        return head

    n, tail = 1, head
    while tail.next:
        n += 1
        tail = tail.next

    x %= n
    if x == 0:
        return head
    
    cur = head
    for _ in range(x - 1):
        cur = cur.next
    new_head = cur.next
    cur.next = None
    tail.next = head
    return new_head

def cyclic_right(head, x):
    if not head:
        return head

    n, tail = 1, head
    while tail.next:
        n += 1
        tail = tail.next

    x %= n
    if x == 0:
        return head

    return cyclic_left(head, n - x)

head = None

while True:
    cmd = list(map(int, input().split()))
     
    if not cmd:
        continue

    if cmd[0] == 0: 
        break
    elif cmd[0] == 1:
        _, x, p = cmd
        head = insert(head, x, p)
    elif cmd[0] == 2:
        _, p = cmd
        head = remove(head, p)
    elif cmd[0] == 3:
        print_linked_list(head)
    elif cmd[0] == 4:
        _, p1, p2 = cmd
        head = replace(head, p1, p2)
    elif cmd[0] == 5:
        head = reverse(head)
    elif cmd[0] == 6:
        _, x = cmd
        head = cyclic_left(head, x)
    elif cmd[0] == 7:
        _, x = cmd
        head = cyclic_right(head, x)