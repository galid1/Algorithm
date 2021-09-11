import sys


def solve():
    global n, e, board

    for stopover in range(1, n+1):
        for start in range(1, n+1):
            if stopover == start:
                continue
            for dest in range(1, n+1):
                if start == dest:
                    continue

                board[start][dest] = min(board[start][dest], board[start][stopover] + board[stopover][dest])


n = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())
board = [[10000001 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(e):
    f, t, v = map(int, sys.stdin.readline().strip().split(" "))
    board[f][t] = min(board[f][t], v)

solve()
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == 10000001:
            board[i][j] = 0
        print(board[i][j], end=' ')
    print()

