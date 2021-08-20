import sys


def solve(n, m):
    s = ""
    for num in range(n, m+1):
        s += str(num)

    ans = 0
    for c in s:
        if c == '0':
            ans += 1

    print(ans)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    solve(n, m)