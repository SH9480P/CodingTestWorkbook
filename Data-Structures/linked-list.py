class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def insert(self, prevNode, value):
        newNode = Node(value)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.size += 1

    def delete(self, prevNode):
        if self.size == 0:
            return
        prevNode.next = prevNode.next.next
        self.size -= 1

    def traverse(self):
        cur = self.head
        while cur.next:
            yield cur.next
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