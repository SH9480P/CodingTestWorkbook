class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def insert(self, prev_node, value):
        newNode = Node(value)
        newNode.next = prev_node.next
        prev_node.next = newNode
        self.size += 1

    def delete(self, prev_node):
        if self.size == 0:
            return
        prev_node.next = prev_node.next.next
        self.size -= 1

    def traverse(self):
        cur = self.head.next
        while cur:
            yield cur
            cur = cur.next

ll = LinkedList()
for i in range(10):
    ll.insert(ll.head, i)

for node in ll.traverse():
    print(node.value)

for i in range(4):
    ll.delete(ll.head)

for node in ll.traverse():
    print(node.value)