import sys


def solve():
    global n, m

    ans = 1
    k = n - m

    while n > k:
        ans *= n
        n -= 1
    while m > 1:
        ans //= m
        m -= 1

    print(ans)


n, m = map(int, sys.stdin.readline().strip().split(" "))
solve()