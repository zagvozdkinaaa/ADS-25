import sys
sys.setrecursionlimit(2000)

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
    
def subtree(x, result):
    if x is None:
        return None
    result.append(x.val)
    subtree(x.left, result)
    subtree(x.right, result)

n = int(input())
nodes = list(map(int, input().split()))
x = int(input())

root = None

for node in nodes:
    root = insert(root, node)

target = find_x(root, x)

result = []
subtree(target, result)
print(*result)