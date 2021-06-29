import sys
from collections import deque


def solution():
    global n
    dq = deque([i for i in range(n, 0, -1)])

    while len(dq) > 1:
        dq.pop()
        dq.appendleft(dq.pop())

    print(dq[-1])


n = int(sys.stdin.readline())
solution()