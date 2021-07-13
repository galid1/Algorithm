import sys

# stack을 이용한 구현
# def dfs(g, start):
#     for key in g.keys():
#         g[key] = sorted(g[key], reverse=True)
#     stack = []
#     stack.append(start)
#
#     visited = set()
#     while stack:
#         cur = stack.pop()
#         if cur in visited:
#             continue
#         # 방문 처리 및 출력
#         print(cur)
#         visited.add(cur)
#
#         for link in g[cur]:
#             stack.append(link)

def dfs(g, vertex, visited):
    print(vertex, end=' ')
    visited.add(vertex)

    for next_vertex in g[vertex]:
        if next_vertex not in visited:
            dfs(g, next_vertex, visited)


n, m, s = map(int, sys.stdin.readline().strip().split(" "))
g = {i: [] for i in range(1, n+1)}
for _ in range(m):
    k, v = map(int, sys.stdin.readline().strip().split(" "))
    g[k].append(v)
    g[v].append(k)

for key in g.keys():
    g[key].sort()

dfs(g, s, set())