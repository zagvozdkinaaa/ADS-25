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

def count_triangles(root):
    if root is None:
        return 0
    count = 0
    if root.left and root.right:
        count += 1
    count += count_triangles(root.left)
    count += count_triangles(root.right)
    return count

n = int(input())
nodes = list(map(int, input().split()))

root = None
for node in nodes:
    root = insert(root, node)

print(count_triangles(root))
