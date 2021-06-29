import sys
from collections import deque


def solve(start):
    global n, g

    q = deque([start])
    visited = [False for _ in range(n+1)]
    visited[start] = True

    ans = [0 for _ in range(n+1)]

    path = 0
    while q:
        path += 1
        for _ in range(len(q)):
            cur = q.popleft()

            for link in g[cur]:
                if not visited[link]:
                    visited[link] = True
                    ans[link] = path
                    q.append(link)

    return ans


n, m = map(int, sys.stdin.readline().strip().split(" "))
g = {i:[] for i in range(1, n+1)}
for _ in range(m):
    f, t = map(int, sys.stdin.readline().strip().split(" "))
    g[f].append(t)
    g[t].append(f)

min_num = sys.maxsize
min_idx = 0
for start in range(1, n+1):
    cavin_num = sum(solve(start))

    if cavin_num < min_num:
        min_num = cavin_num
        min_idx = start

print(min_idx)