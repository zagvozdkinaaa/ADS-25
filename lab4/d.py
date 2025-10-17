from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def sum_on_level(root):
    if root is None:
        return []

    result = []
    q = deque([(root, 0)])

    while q:
        node, lvl = q.popleft()
        if lvl == len(result):
            result.append(0) 
        result[lvl] += node.val

        if node.left:
            q.append((node.left, lvl+1))
        if node.right:
            q.append((node.right, lvl+1))

    return result

n = int(input())
nodes = list(map(int, input().split()))

root = None
for node in nodes:
    root = insert(root, node)

result = sum_on_level(root)

print(len(result))
print(*result)
