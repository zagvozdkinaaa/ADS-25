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

def find_max_sum(head):
    current = head
    max_sum = head.value
    current_sum = 0
    while current:
        current_sum += current.value
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
        current = current.next

    return max_sum

n = int(input())
arr = list(map(int, input().split()))
head = build_linked_list(arr)
print(find_max_sum(head))

