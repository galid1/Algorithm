import sys
from collections import deque


def solve():
    global n, logs

    logs.sort()

    new_logs = deque()
    for i in range(len(logs)):
        if i % 2 == 0:
            new_logs.appendleft(logs[i])
        else:
            new_logs.append(logs[i])


    idx = 0
    max_sub = 0
    while idx < len(new_logs):
        max_sub = max(max_sub, abs(new_logs[idx] - new_logs[(idx+1)%len(new_logs)]))
        idx += 1

    print(max_sub)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    logs = list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()

# 3
# 7
# 13 10 12 11 10 11 12
# 5
# 2 4 5 7 9
# 8
# 6 6 6 6 6 6 6 6
