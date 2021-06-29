import sys

def solve():
    global n, ts

    d = [[0 for _ in range(n)] for _ in range(n+1)]
    d[1][0] = ts[1][0]

    for i in range(2, n+1):
        for j in range(i):
            if 1 <= j < i-1:
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + ts[i][j]
            elif j == 0:
                d[i][j] = d[i-1][0] + ts[i][0]
            elif j == i-1:
                d[i][j] = d[i-1][j-1] + ts[i][j]

    print(max(d[n]))


n = int(sys.stdin.readline().strip())
ts = [[]]
for i in range(n):
    ts.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()

# 3
# 8
# 1 3
# 4 2 5