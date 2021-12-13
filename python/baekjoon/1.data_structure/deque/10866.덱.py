import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Deque:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def append_head(self, val):
        new_node = Node(val)
        self.size += 1

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.right = self.head
        self.head.left = new_node
        self.head = new_node

    def append_tail(self, val):
        new_node = Node(val)
        self.size += 1

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.right = new_node
        new_node.left = self.tail
        self.tail = new_node

    def pop_head(self):
        if self.is_empty():
            return -1

        self.size -= 1

        tmp = self.head.val

        if self.head.right is None:
            self.head = self.tail = None
        else:
            self.head = self.head.right
            self.head.left = None

        return tmp

    def pop_tail(self):
        if self.is_empty():
            return -1

        self.size -= 1

        tmp = self.tail.val

        if self.tail.left is None:
            self.tail = self.head = None
        else:
            self.tail = self.tail.left
            self.tail.right = None

        return tmp

    def is_empty(self):
        return 1 if self.head is None else 0

    def get_size(self):
        return self.size

    def front(self):
        if self.is_empty():
            return -1

        return self.head

    def back(self):
        if self.is_empty():
            return -1

        return self.tail

    def print_dq(self):
        t_h = self.head
        while t_h:
            print(t_h.val, '->', end=' ')
            t_h = t_h.right


def solve():
    global n, cmds

    deque = Deque()

    for cmd in cmds:
        if cmd[0] == "front":
            if deque.front() == -1:
                print(-1)
            else:
                print(deque.front().val)

        elif cmd[0] == "back":
            if deque.back() == -1:
                print(-1)
            else:
                print(deque.back().val)

        elif cmd[0] == "size":
            print(deque.get_size())

        elif cmd[0] == "empty":
            print(deque.is_empty())

        elif cmd[0] == "push_front":
            deque.append_head(int(cmd[1]))

        elif cmd[0] == "push_back":
            deque.append_tail(int(cmd[1]))

        elif cmd[0] == "pop_front":
            print(deque.pop_head())

        elif cmd[0] == "pop_back":
            print(deque.pop_tail())


n = int(sys.stdin.readline().strip())
cmds = []
for _ in range(n):
    cmds.append(sys.stdin.readline().strip().split(" "))

solve()
