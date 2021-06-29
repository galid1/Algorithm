import sys


def solution():
    global ts, ps

    for i in range(n+1):
        d[i] = max(d[i], d[i-1])

        if i + ts[i] <= n+1:
            d[i+ts[i]] = max(d[i+ts[i]], d[i] + ps[i])


n = int(sys.stdin.readline())
ts, ps = [0], [0]
d = [0 for i in range(n+2)]
for i in range(n):
    t, p = map(int, sys.stdin.readline().strip().split(" "))
    ts.append(t)
    ps.append(p)

solution()
print(max(d))
