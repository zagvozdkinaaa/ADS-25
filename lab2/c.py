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

def delete_every_second(head):
    current = head 
    while current and current.next:
        current.next = current.next.next
        current = current.next
    return head

def print_linked_list(head):
    current = head 
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    print(' '.join(result))

n = int(input())

arr = list(map(int, input().split()))

head = build_linked_list(arr)

head = delete_every_second(head)

print_linked_list(head)