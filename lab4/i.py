import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key == node.key:
            node.count += 1
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.count > 1:
                node.count -= 1
                return node
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self._minValueNode(node.right)
            node.key = temp.key
            node.count = temp.count
            temp.count = 1
            node.right = self._delete(node.right, temp.key)
        return node

    def _minValueNode(self, node):
        while node.left:
            node = node.left
        return node

    def cnt(self, key):
        return self._cnt(self.root, key)

    def _cnt(self, node, key):
        if not node:
            return 0
        if key == node.key:
            return node.count
        elif key < node.key:
            return self._cnt(node.left, key)
        else:
            return self._cnt(node.right, key)


bst = BST()
input_data = sys.stdin.read().strip().split("\n")
for line in input_data[1:]:
    cmd, x = line.split()
    x = int(x)
    if cmd == "insert":
        bst.insert(x)
    elif cmd == "delete":
        bst.delete(x)
    else:
        print(bst.cnt(x))
