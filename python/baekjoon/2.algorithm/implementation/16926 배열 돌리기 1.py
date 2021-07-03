import sys


def recur(x, y):
    global n, m

    while x < n//2 and y < m//2:
        solve(x, y)
        x, y = x+1, y+1


def solve(x, y):
    global n, m, board

    temp_start = board[x][y]

    #윗줄 이동
    for i in range(y, m-1-y):
        board[x][i] = board[x][i+1]

    #오른쪽줄 위로
    for i in range(x, n-1-x):
        board[i][m-1-y] = board[i+1][m-1-y]

    #아랫줄 이동
    for i in range(m-1-y, y-1, -1):
        board[n-1-x][i] = board[n-1-x][i-1]

    #왼쪽 줄 이동
    for i in range(n-1-x, x+1, -1):
        board[i][y] = board[i-1][y]

    board[x+1][y] = temp_start


n, m, r = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

r = r%(n*m)
for _ in range(r):
    recur(0, 0)

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()

# 4 5 1
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
#
# 2 2 10
# 1 1
# 2 2
#
# 2 6 1
# 1 2 3 4 5 6
# 7 8 9 10 11 12

# 6 7 1
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7

# 4 5 1
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
