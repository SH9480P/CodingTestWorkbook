class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertBefore(self, node, value):
        if node == self.head:
            return
        newNode = Node(value)
        newNode.prev = node.prev
        node.prev.next = newNode
        newNode.next = node
        node.prev = newNode
        self.size += 1

    def insertAfter(self, node, value):
        if node == self.tail:
            return
        newNode = Node(value)
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode
        newNode.prev = node
        self.size += 1

    def delete(self, node):
        if node == self.head or node == self.tail:
            return
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1

    def traverse(self):
        cur = self.head.next
        while cur != self.tail:
            yield cur
            cur = cur.next


dll = DoublyLinkedList()

for i in range(10):
    dll.insertAfter(dll.head, i)

result = []
for node in dll.traverse():
    result.append(node.value)
print(result)
for i in range(3):
    dll.delete(dll.tail.prev.prev)

result = []
for node in dll.traverse():
    result.append(node.value)
print(result)