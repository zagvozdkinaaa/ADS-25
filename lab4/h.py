class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def transform(root):
    s = 0
    def dfs(node):
        nonlocal s
        if not node:
            return
        dfs(node.right)
        s += node.val
        node.val = s
        dfs(node.left)
    dfs(root)

def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

n = int(input())
arr = list(map(int, input().split()))
root = None
for v in arr:
    root = insert(root, v)
transform(root)
res = []
inorder(root, res)
print(*reversed(res))