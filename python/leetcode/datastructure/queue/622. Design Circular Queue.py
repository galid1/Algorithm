class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [-1 for _ in range(k+1)]
        self.front, self.rear = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear+1)%len(self.queue)
        self.queue[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front+1)%len(self.queue)
        self.queue[self.front] = -1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.front+1)%len(self.queue)]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1)%len(self.queue) == self.front


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.deQueue())
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.Front())
print(obj.Rear())
print(obj.isEmpty())
print(obj.isFull())
print(obj.enQueue(4))
print(obj.enQueue(5))
print(obj.deQueue())