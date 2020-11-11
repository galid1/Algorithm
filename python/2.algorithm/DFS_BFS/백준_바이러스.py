import sys


def solution():
    global g, v

    s = [1]
    v[1] = 1
    ans = 0

    while s:
        cur = s.pop()
        ans += 1

        for l in g[cur]:
            if not v[l]:
                s.append(l)
                v[l] = 1

    print(ans-1)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
g = {k:set([]) for k in range(1, n+1)}
v = [0 for i in range(0, n+1)]
for i in range(m):
    k, l = map(int, sys.stdin.readline().strip().split(" "))
    g[k].add(l)
    g[l].add(k)

solution()
