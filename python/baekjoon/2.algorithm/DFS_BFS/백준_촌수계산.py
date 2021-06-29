import sys
from collections import deque


def solution():
    global g, n, m, ta, tb
    v = [0 for _ in range(n+1)]
    answer = -1
    q =  deque()
    q.append(ta)
    v[ta] = 1

    while q:
        answer += 1

        for i in range(len(q)):
            cur = q.popleft()
            # 정답
            if cur == tb:
                print(answer)
                return

            for link in g[cur]:
                if not v[link]:
                    q.append(link)
                    v[link] = 1

    print(-1)


n = int(sys.stdin.readline())
ta, tb = map(int, sys.stdin.readline().strip().split(" "))
m = int(sys.stdin.readline())
g = {i:[] for i in range(1, n+1)}

for _ in range(m):
    parent, child = map(int, sys.stdin.readline().strip().split(" "))
    g[parent].append(child)
    g[child].append(parent)

solution()
