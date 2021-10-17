import sys


def solve(n, ps):
    ps.sort()

    ans = 0
    c_sum = 0

    for num in ps:
        c_sum += num
        ans += c_sum

    print(ans)


n = int(sys.stdin.readline().strip())
ps = list(map(int, sys.stdin.readline().strip().split(" ")))
solve(n, ps)