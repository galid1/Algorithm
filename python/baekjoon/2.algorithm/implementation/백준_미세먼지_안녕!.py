import sys


def solve():
    global n, m, t, board

    while t > 0:
        t -= 1
        spread_dust()
        run_air_cond()

    answer = 0
    for i in range(n):
        for j in range(m):
            value = board[i][j]
            if value != -1:
                answer += value

    print(answer)


def run_air_cond():
    global n, m, board, ds, air_cond

    ux = air_cond[0]
    dx = air_cond[1]

    for i in range(ux-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(0, m-1):
        board[0][i] = board[0][i+1]
    for i in range(0, ux):
        board[i][m-1] = board[i+1][m-1]
    for i in range(m-1, 1, -1):
        board[ux][i] = board[ux][i-1]
    board[ux][1] = 0

    for i in range(dx+1, n-1):
        board[i][0] = board[i+1][0]
    for i in range(0, m-1):
        board[n-1][i] = board[n-1][i+1]
    for i in range(n-1, dx-1, -1):
        board[i][m-1] = board[i-1][m-1]
    for i in range(m-1, 1, -1):
        board[dx][i] = board[dx][i-1]
    board[dx][1] = 0



def spread_dust():
    global n, m, board, ds

    spreads = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] > 4:
                move_dust_amount = board[i][j] // 5

                for dx, dy in ds:
                    nx, ny = i+dx, j+dy

                    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == -1:
                        continue

                    board[i][j] -= move_dust_amount
                    spreads[nx][ny] += move_dust_amount

    for i in range(n):
        for j in range(m):
            board[i][j] += spreads[i][j]


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m, t = map(int, sys.stdin.readline().strip().split(" "))
air_cond = []
board = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    if line[0] == -1:
        air_cond.append(i)
    board.append(line)
solve()