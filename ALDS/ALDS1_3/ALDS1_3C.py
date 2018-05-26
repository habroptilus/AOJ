# これもdeque使わないと時間切れになるのか？
from sys import stdin


class Node():
    def __init__(self,  key=None, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList():
    def __init__(self):
        head = Node()
        head.next = head
        head.prev = head
        self.size = 0
        self.head = head

    def insert(self, x):
        node = Node(key=x, prev=self.head, next=self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def delete(self, x):
        node = self.head.next
        while node is not self.head:
            if node.key == x:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                break
            node = node.next

    def deleteFirst(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1

    def deleteLast(self):
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev
        self.size -= 1

    def getKeys(self):
        node = self.head.next
        keys = []
        while node is not self.head:
            keys.append(str(node.key))
            node = node.next
        return " ".join(keys)


L = DoublyLinkedList()
n = int(input())
for i in range(n):
    command = stdin.readline().strip().split()
    if command[0] == "insert":
        L.insert(int(command[1]))
    elif command[0] == "delete":
        L.delete(int(command[1]))
    elif command[0] == "deleteFirst":
        L.deleteFirst()
    else:
        L.deleteLast()

print(L.getKeys())
