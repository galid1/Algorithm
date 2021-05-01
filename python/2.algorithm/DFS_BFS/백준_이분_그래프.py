import sys
from collections import deque
# 두 그룹으로 나누고, 같은 그룹에 속한 정점이 연결되어 있지 않아야 하는 문제


def solve():
    global g, v, e

    visited = [0 for _ in range(v+1)]

    # 정점이 끊겨 있을 수도 있기 때문에 전체 반복
    for i in range(1, v+1):
        if visited[i] > 0:
            continue

        q = deque([i])
        cur_paint = 1
        visited[i] = cur_paint

        while q:
            cur_paint = 2 if cur_paint == 1 else 1

            for _ in range(len(q)):
                cv = q.popleft()

                for link in g[cv]:
                    if visited[link] > 0:
                        if visited[link] == visited[cv]:
                            return print("NO")
                        continue

                    visited[link] = cur_paint
                    q.append(link)

    return print("YES")


k = int(sys.stdin.readline().strip())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().strip().split(" "))
    g = {i:[] for i in range(1, v+1)}

    for _ in range(e):
        f, t = map(int, sys.stdin.readline().strip().split(" "))
        g[f].append(t)
        g[t].append(f)

    solve()
