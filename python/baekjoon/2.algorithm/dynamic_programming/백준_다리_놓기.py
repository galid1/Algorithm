import sys


def solve():
    global n, m

    print(d[n][m])



d = [[0 for _ in range(31)] for _ in range(31)]
for i in range(1, 31):
    d[1][i] = i
    d[i][i] = 1

for i in range(2, 31):
    for j in range(i+1, 31):
        for mi in range(1, j-i+1+1):
            d[i][j] += d[i-1][j-mi]

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    solve()