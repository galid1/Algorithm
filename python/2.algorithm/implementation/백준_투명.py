import sys


def solve():
    global n, m, papers

    board = [[0 for _ in range(100)] for _ in range(100)]

    for sx, sy, ex, ey in papers:
        for x in range(sx-1, ex):
            for y in range(sy-1, ey):
                board[x][y] += 1

    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] > m:
                cnt +=1
    print(cnt)

n, m = map(int, sys.stdin.readline().strip().split(" "))
papers = []
for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()