import sys

def solve():
    global n, m, board

    res = 0
    for i in range(n):
        for j in range(m):
            # ㅡ
            if j + 3 < m:
                res = max(res, board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3])
            # ㅣ
            if i + 3 < n:
                res = max(res, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])

            # ㅁ
            if i+1 < n and j+1 < m:
                res = max(res, board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1])

            # L
            if i+2 < n and j+1 < m:
                res = max(res, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1])
                res = max(res, board[i+2][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1])
                res = max(res, board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1])
                res = max(res, board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j])
            # ㄴ
            if i+1 < n and j+2 < m:
                res = max(res, board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j])
                res = max(res, board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2])
                res = max(res, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2])
                res = max(res, board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2])

            # ㄴㄱ
            if i+2 < n and j+1 < m:
                res = max(res, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1])
                res = max(res, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])

            if i+1 < n and j+2 < m:
                res = max(res, board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1])
                res = max(res, board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2])

            # ㅗ
            if i+1 < n and j+2 < m:
                res = max(res, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2])
                res = max(res, board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1])

            if i+2 < n and j+1 < m:
                res = max(res, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])
                res = max(res, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1])

    print(res)

n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()