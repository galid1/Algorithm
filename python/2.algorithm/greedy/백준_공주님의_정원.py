import sys

def solve():
    global n, ds

    ls, le = 301, 301
    ans, idx = 0, 0

    while idx < n:
        s, e = ds[idx]

        if s > le:
            break

        idx += 1
        while idx < n:
            ts, te = ds[idx]
            if ts > le:
                break
            if te > e:
                s, e = ts, te
            idx += 1

        ans += 1
        ls, le = s, e

        if le > 1130:
            break

    if le <= 1130:
        print(0)
    else:
        print(ans)

n = int(sys.stdin.readline().strip())
ds = []
for _ in range(n):
    sm, sd, em, ed = list(map(int, sys.stdin.readline().strip().split(" ")))
    ds.append((sm*100 + sd, em*100 + ed))
ds.sort()
solve()