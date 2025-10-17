import sys
sys.setrecursionlimit(300000)

class Node:
    __slots__ = ("data", "left", "right")
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.diameter = 0

    def insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.data:
            node.left = self.insert(node.left, val)
        elif val > node.data:
            node.right = self.insert(node.right, val)
        return node

    def insert_value(self, val):
        self.root = self.insert(self.root, val)

    def depth(self, node):
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        # обновляем диаметр (считаем рёбра)
        self.diameter = max(self.diameter, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    def get_diameter(self):
        self.diameter = 0
        self.depth(self.root)
        return self.diameter + 1 

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    tree = BST()
    for x in arr:
        tree.root = tree.insert(tree.root, x)

    print(tree.get_diameter())

if __name__ == "__main__":
    main()