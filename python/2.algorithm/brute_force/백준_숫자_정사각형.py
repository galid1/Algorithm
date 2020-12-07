import sys


def solution():
    global n, m, board, max_size

    for i in range(n - 1):
        for j in range(m - 1):
            last = min(m - j, n - i)
            for k in range(1, last):
                if board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]:
                    max_size = max(max_size, pow(k+1, 2))

    print(max_size)

max_size = 1
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))
solution()

