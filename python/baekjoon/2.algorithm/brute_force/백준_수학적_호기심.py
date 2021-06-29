import sys


def solve():
    global n, m

    ans = 0
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            num = (pow(a, 2) + pow(b, 2) + m)
            if num % (a*b) == 0:
                ans += 1
    print(ans)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    solve()


# 1
# 10 1