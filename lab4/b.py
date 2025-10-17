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

def find_x(root, x):
    if root is None:
        return None
    if x == root.val:
        return root
    elif x < root.val:
        return find_x(root.left, x)
    else:
        return find_x(root.right, x)

def subtree_size(x):
    if x is None:
        return 0
    return 1 + subtree_size(x.left) + subtree_size(x.right)

n = int(input())
nodes = list(map(int, input().split()))
x = int(input())

root = None

for node in nodes:
    root = insert(root, node)

target = find_x(root, x)

print(subtree_size(target))