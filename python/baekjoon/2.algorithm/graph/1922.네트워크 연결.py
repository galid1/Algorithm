import sys, heapq


def solve():
    global n, m, es

    sets = [i for i in range(n+1)]
    ans = 0
    while es:
        w, f, t = heapq.heappop(es)

        if find(f, sets) == find(t, sets):
            continue

        union(f, t, sets)
        ans += w

    print(ans)


def find(v, sets):
    if v == sets[v]:
        return v

    root = find(sets[v], sets)
    sets[v] = root
    return root


def union(v1, v2, sets):
    p1 = find(v1, sets)
    p2 = find(v2, sets)

    if p1 < p2:
        sets[p2] = p1
    else:
        sets[p1] = p2


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
es = []
for _ in range(m):
    f, t, w = map(int, sys.stdin.readline().strip().split(" "))
    heapq.heappush(es, (w, f, t))

solve()