import sys
from collections import deque

def solution():
    find_circular()
    cal_distance()


def cal_distance():
    global g, n, cs, ans

    for i in range(1, n+1):
        if cs[i]:
            print(0, end = ' ')
            continue

        visit = [0 for _ in range(n+1)]
        q = deque()
        q.append((i, 0))
        found = False

        while q:
            cur_v, cur_d = q.pop()
            visit[cur_v] = True

            for link in g[cur_v]:
                if cs[link]:
                    print(cur_d + 1, end=' ')
                    found = True
                    break

                if not visit[link]:
                    q.append((link, cur_d+1))

            if found:
                break


def find_circular():
    global g, n
    for k in g.keys():
        g[k] = sorted(g[k], reverse=True)

    for i in range(1, n+1):
        # 이미 순환임을 알아냄
        if cs[i]:
            continue

        stack = [i]
        visit = [False for _ in range(n+1)]
        ds = [0 for _ in range(n+1)]
        found = False

        while stack:
            v = stack.pop()
            visit[v] = True

            for link in g[v]:
                if visit[link] and ds[v]+1 - ds[link] > 2:
                    cs[link] = True
                    found = True
                    break

                if not visit[link]:
                    stack.append(link)
                    ds[link] = ds[v]+1

            if found:
                break


g = {}
n = int(sys.stdin.readline())
ans = [0 for _ in range(n+1)]
cs = [0 for _ in range(n+1)]
for i in range(n):
    f, t = map(int, sys.stdin.readline().strip().split(" "))

    if f not in g.keys():
        g[f] = [t]
    else:
        g[f].append(t)
    if t not in g.keys():
        g[t] = [f]
    else:
        g[t].append(f)

solution()