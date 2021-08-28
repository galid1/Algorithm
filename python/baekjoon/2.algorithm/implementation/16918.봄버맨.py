import sys


def solve():
    global r, c, n, board

    # board 순회하며 폭탄 위치 찾기
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                board[i][j] = 0

    time = 1

    is_lay_time = True
    while time < n:
        time += 1

        if is_lay_time:
            lay_bomb(time)
            is_lay_time = False
        else:
            bomb(time)
            is_lay_time = True

    # result
    for i in range(r):
        for j in range(c):
            if board[i][j] != '.':
                print('O', end='')
            else:
                print(board[i][j], end='')
        print()


def lay_bomb(time):
    global r, c, board

    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = time


def bomb(cur_time):
    global r, c, board, ds

    stack = []

    for i in range(r):
        for j in range(c):
            if board[i][j] != '.' and board[i][j] + 3 == cur_time:
                board[i][j] = '.'
                stack.append([i, j])

    while stack:
        cx, cy = stack.pop()

        for dx, dy in ds:
            nx, ny = cx+dx, cy+dy

            if not valid(nx, ny):
                continue

            board[nx][ny] = '.'


def valid(x, y):
    global r, c
    return 0 <= x < r and 0 <= y < c


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
r, c, n = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))

solve()

# 6 7 3
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....