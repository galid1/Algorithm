import sys
from collections import deque


def solve():
    global n, m, fs

    visited = [False for _ in range(n+1)]
    visited[1] = True
    q = deque([1])
    count = 0
    answer = 0
    while q:
        count += 1
        if count > 2:
            return print(answer)

        for _ in range(len(q)):
            c = q.popleft()

            for friend in fs[c]:
                if not visited[friend]:
                    visited[friend] = True
                    answer += 1
                    q.append(friend)


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
fs = {i:[] for i in range(1, n+1)}
for _ in range(m):
    f, t = map(int, sys.stdin.readline().strip().split(" "))
    fs[f].append(t)
    fs[t].append(f)

solve()