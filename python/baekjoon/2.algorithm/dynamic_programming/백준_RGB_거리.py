import sys

def solve():
    global n, rgbs

    # r ,g ,b 선
    d = [[1001 for _ in range(3)] for _ in range(n+1)]
    d[0][0] = 0
    d[0][1] = 0
    d[0][2] = 0

    # d[i][0] == i번째 집을 R로 칠했을 때 가장 작은 값
    for i in range(1, n+1):
        d[i][0] = rgbs[i][0] + min(d[i-1][1], d[i-1][2])
        d[i][1] = rgbs[i][1] + min(d[i-1][0], d[i-1][2])
        d[i][2] = rgbs[i][2] + min(d[i-1][0], d[i-1][1])

    print(min(d[n][0], d[n][1], d[n][2]))


n = int(sys.stdin.readline().strip())
rgbs = [0]
for i in range(n):
    rgbs.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()