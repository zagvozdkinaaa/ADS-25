class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_linked_list(arr):
    head = Node(arr[0])
    current = head
    for num in arr[1:]:
        current.next = Node(num)
        current = current.next
    return head

def print_linked_list(head):
    current = head 
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    print(' '.join(result))

def insert_node(head, data, pos):
    new_node = Node(data)
    if pos == 0:
        new_node.next = head
        return new_node
    
    current = head

    for i in range(pos - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head

n = int(input())
arr = [int(input()) for i in range(n)]
data = int(input())
pos = int(input())

head = build_linked_list(arr)
head = insert_node(head, data, pos)
print_linked_list(head)
