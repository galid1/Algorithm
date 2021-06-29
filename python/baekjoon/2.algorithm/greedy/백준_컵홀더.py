import sys

def solve():
    global n, ps

    ans = 1
    idx = 0
    while idx <= n-1:
        if ps[idx] == 'S':
            idx += 1
            ans += 1
        else:
            idx += 2
            ans += 1

    print(min(ans, n))

n = int(sys.stdin.readline().strip())
ps = list(sys.stdin.readline().strip())
solve()