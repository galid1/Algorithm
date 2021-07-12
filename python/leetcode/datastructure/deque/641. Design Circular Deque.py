class DoubleListNode:
    def __init__(self, val, next=None, bef=None):
        self.val = val
        self.next = next
        self.bef = bef


class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.length = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DoubleListNode(value)

        if self.isEmpty():
            self.length += 1
            self.head = self.tail = new_node
            return True

        self.length += 1
        new_node.next = self.head
        self.head.bef = new_node
        self.head = new_node
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DoubleListNode(value)

        if self.isEmpty():
            self.length += 1
            self.head = self.tail = new_node
            return True

        self.length += 1
        self.tail.next = new_node
        new_node.bef = self.tail
        self.tail = new_node
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.length -= 1
        self.head = self.head.next
        if self.head:
            self.head.bef = None
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.length -= 1
        self.tail = self.tail.bef

        if self.tail:
            self.tail.next = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
print(obj.insertFront(1))
print(obj.insertLast(4))
print(obj.deleteFront())
print(obj.deleteLast())
print(obj.getFront())
print(obj.getRear())
print(obj.isEmpty())
print(obj.isFull())