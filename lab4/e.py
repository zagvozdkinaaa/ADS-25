from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_width(root):
    if root is None:
        return []

    result = []
    q = deque([(root, 0)])

    while q:
        node, lvl = q.popleft()
        if lvl == len(result):
            result.append(0) 
        result[lvl] += 1

        if node.left:
            q.append((node.left, lvl+1))
        if node.right:
            q.append((node.right, lvl+1))

    return max(result)

n = int(input())
nodes = {i: Node(i) for i in range(1, n+1)}

for i in range(n-1):
    x, y, z = map(int, input().split())
    if z == 0:
        nodes[x].left = nodes[y]
    else:
        nodes[x].right = nodes[y]

root = nodes[1]

print(max_width(root))
