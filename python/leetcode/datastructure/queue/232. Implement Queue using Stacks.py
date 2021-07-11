class MyQueue:
    def __init__(self):
        self.s1, self.s2 = [], []
        self.size = 0
        self.front = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()

        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]

        return self.front

    def empty(self) -> bool:
        return not self.s1 and not self.s2


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.peek())
print(obj.empty())

