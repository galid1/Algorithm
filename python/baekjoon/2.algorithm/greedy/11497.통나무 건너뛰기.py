import sys
from collections import deque


def solve():
    global n, logs

    logs.sort()

    q = deque()
    idx = 0
    while logs:
        idx += 1
        log = logs.pop()

        if idx %2 != 0:
            q.appendleft(log)
        else:
            q.append(log)

    ans = 0
    for i in range(-1, n-1):
        ans = max(abs(q[i] - q[i+1]), ans)

    print(ans)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    logs = list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()