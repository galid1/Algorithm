from collections import deque

class MyStack:
    def __init__(self):
        self.q1, self.q2 = deque(), deque()
        self.size = 0
        self.top_val = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size += 1
        self.top_val = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            top = self.q1.popleft()
            self.q2.append(top)
            self.top_val = top

        self.q1, self.q2 = self.q2, self.q1
        if len(self.q2) == 1:
            self.size -= 1

        return self.q2.pop()

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return self.size <= 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.top())
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

