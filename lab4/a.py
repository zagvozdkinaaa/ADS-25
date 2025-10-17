import sys
sys.setrecursionlimit(200000)

class Node:
    __slots__ = ("val", "left", "right")
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    cur = root
    while True:
        if val < cur.val:
            if cur.left is None:
                cur.left = Node(val)
                return
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node(val)
                return
            cur = cur.right

def check_path(root, path):
    node = root
    for turn in path:
        if node is None:
            return "NO"
        if turn == 'L':
            node = node.left
        else:
            node = node.right
    return "YES" if node else "NO"

data = sys.stdin.read().strip().split()
n, m = int(data[0]), int(data[1])
nums = list(map(int, data[2:2+n]))
paths = data[2+n:]

root = Node(nums[0])
for num in nums[1:]:
    insert(root, num)

out = []
for p in paths:
    out.append(check_path(root, p))
print("\n".join(out))
