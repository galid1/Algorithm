import sys


def solve():
    global n, arr

    arr.sort(key=lambda item: (item[0], item[1]))

    ans = 0
    idx = 0
    while idx < n:
        cs, ce = arr[idx]

        jdx = idx+1
        while jdx < n:
            ts, te = arr[jdx]

            if ts > ce:
                break

            if te > ce:
                ce = te

            jdx += 1

        idx += (jdx - idx)
        ans += ce - cs

    print(ans)


n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().strip().split(" "))))

solve()


# 4
# 1 3
# 2 2
# 4 5
# 6 7