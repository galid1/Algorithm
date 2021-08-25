import sys


def solve(n, ts):
    ans, max_t = 0, -1

    ts.sort(reverse=True)

    for t in ts:
        ans += 1

        if max_t - 1 < t:
            max_t = t
        else:
            max_t -= 1

    print(ans + max_t + 1)


n = int(sys.stdin.readline().strip())
ts = list(map(int, sys.stdin.readline().strip().split(" ")))
solve(n, ts)
