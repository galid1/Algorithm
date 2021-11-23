import sys


def solve():
    global n, ls

    ls.sort()

    min_diff = sys.maxsize
    ans = -1, -1

    for L in range(n-1):
        s = L+1
        e = len(ls) - 1

        while s <= e:
            R = (s + e) // 2

            res = ls[L] + ls[R]

            if res == 0:
                return print(ls[L], ls[R])

            if abs(res) < min_diff:
                min_diff = abs(res)
                ans = ls[L], ls[R]

            if res > 0:
                e = R - 1
            else:
                s = R + 1

    print(ans[0], ans[1])


n = int(sys.stdin.readline().strip())
ls = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()


# 6
# -2 4 -99 -1 98 1