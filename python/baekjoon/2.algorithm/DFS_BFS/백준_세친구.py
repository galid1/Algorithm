import sys

def solve():
    global rs

    ans = sys.maxsize
    for i in range(n+1):
        for j in range(i+1, n+1):
            if rs[i][j]:
                for k in range(j+1, n+1):
                    if rs[i][k] and rs[j][k]:
                        ans = min(ans, cal_friends(i, j, k))

    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)


def cal_friends(i, j, k):
    global cnts

    return cnts[i] + cnts[j] + cnts[k] - 6


n, m = map(int, sys.stdin.readline().strip().split(" "))
rs = [[False for _ in range(n+1)] for _ in range(n+1)]
cnts = {i:0 for i in range(1, n+1)}
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    rs[a][b] = True
    rs[b][a] = True
    cnts[a] += 1
    cnts[b] += 1

solve()
