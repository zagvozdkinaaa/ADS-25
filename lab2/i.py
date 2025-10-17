class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("ok")

    def add_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print("ok")

    def erase_front(self):
        if self.head is None:
            print("error")
            return
        print(self.head.value)
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def erase_back(self):
        if self.tail is None:
            print("error")
            return
        print(self.tail.value)
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def front(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.value)

    def back(self):
        if self.tail is None:
            print("error")
        else:
            print(self.tail.value)

    def clear(self):
        self.head = self.tail = None
        print("ok")


dll = DoublyLinkedList()

while True:
    command = input().split()
    if command[0] == "add_front":
        dll.add_front(command[1])
    elif command[0] == "add_back":
        dll.add_back(command[1])
    elif command[0] == "erase_front":
        dll.erase_front()
    elif command[0] == "erase_back":
        dll.erase_back()
    elif command[0] == "front":
        dll.front()
    elif command[0] == "back":
        dll.back()
    elif command[0] == "clear":
        dll.clear()
    elif command[0] == "exit":
        print("goodbye")
        break

