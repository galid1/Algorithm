import sys
from collections import deque


def solve():
    global n, m, g

    max_cnt = 0
    ms = []

    for start in range(1, n+1):
        visited = [False for _ in range(n+1)]

        q = deque([start])
        visited[start] = True
        cnt = 1

        while q:
            cv = q.popleft()

            for link in g[cv]:
                if visited[link]:
                    continue

                visited[link] = True
                cnt += 1
                q.append(link)

        if cnt > max_cnt:
            max_cnt = cnt
            ms = [start]
        elif cnt == max_cnt:
            ms.append(start)

    ms.sort()
    print(*ms)


n, m = map(int, sys.stdin.readline().strip().split(" "))
g = {i:set() for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    g[b].add(a)


solve()

# 3 3
# 3 1
# 2 1
# 3 2