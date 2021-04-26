import sys

def solve():
    global n, hs

    ans = 0
    cur_h = 0
    cnt = 0
    for i in range(n):
        if cur_h > hs[i]:
            cnt += 1
        else:
            cur_h = hs[i]
            ans = max(ans, cnt)
            cnt = 0

    print(max(ans, cnt))


n = int(sys.stdin.readline().strip())
hs = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()

