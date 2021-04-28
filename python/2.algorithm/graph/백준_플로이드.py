import sys


def solve():
    global n, m, g

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if j == k:
                    continue

                transfer = g[j][i] + g[i][k]
                if g[j][k] > transfer:
                    g[j][k] = transfer

    for l in g:
        for num in l:
            if num == 100001:
                print(0, end=' ')
                continue
            print(num, end=' ')
        print()


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
g = [[100001 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    f, t, v = map(int, sys.stdin.readline().strip().split(" "))
    g[f-1][t-1] = min(g[f-1][t-1], v)

solve()

# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0