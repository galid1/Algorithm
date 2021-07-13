import sys
from collections import deque


def bfs(g, vertex, visited):
    queue = deque()
    queue.append(vertex)
    visited.add(vertex)

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for next_vertex in g[cur]:
            if next_vertex not in visited:
                queue.append(next_vertex)
                visited.add(next_vertex)


n, m, s = map(int, sys.stdin.readline().strip().split(" "))
g = {i: [] for i in range(1, n+1)}
for _ in range(m):
    k, v = map(int, sys.stdin.readline().strip().split(" "))
    g[k].append(v)
    g[v].append(k)

for key in g.keys():
    g[key].sort()

bfs(g, s, set())