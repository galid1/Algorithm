import sys


def solve():
    global board

    # 돌을 처음부터 끝까지 놓을 수 있는 자리에 놓고 검사
    for i in range(10):
        for j in range(10):
            if board[i][j] != '.':
                continue

            if clear(i, j):
                return print(1)

    print(0)


def clear(i, j):
    global board

    return check_hor(board, i, j) \
           or check_ver(board, i, j) \
           or check_r_diagonal(board, i, j) or check_l_diagonal(board, i, j)


def check_hor(board, i, j):
    cnt = 0
    nj = j
    while True:
        if not valid(i, nj - 1):
            break

        if board[i][nj - 1] != 'X':
            break

        cnt += 1
        nj -= 1

    nj = j
    while True:
        if not valid(i, nj + 1):
            break

        if board[i][nj + 1] != 'X':
            break

        cnt += 1
        nj += 1

    return cnt >= 4


def check_ver(board, i, j):
    cnt = 0
    ni = i
    while True:
        if not valid(ni - 1, j):
            break

        if board[ni - 1][j] != 'X':
            break

        ni -= 1
        cnt += 1

    ni = i
    while True:
        if not valid(ni + 1, j):
            break

        if board[ni + 1][j] != 'X':
            break

        ni += 1
        cnt += 1

    return cnt >= 4


def check_r_diagonal(board, i, j):
    # 우하향 대각선
    cnt = 0
    ni, nj = i, j
    while True:
        if not valid(ni - 1, nj - 1):
            break

        if board[ni - 1][nj - 1] != 'X':
            break

        cnt += 1
        ni, nj = ni - 1, nj - 1

    ni, nj = i, j
    while True:
        if not valid(ni + 1, nj + 1):
            break

        if board[ni + 1][nj + 1] != 'X':
            break

        cnt += 1
        ni, nj = ni + 1, nj + 1

    return cnt >= 4

def check_l_diagonal(board, i, j):
    # 좌하향 대각선
    cnt = 0
    ni, nj = i, j
    while True:
        if not valid(ni - 1, nj + 1):
            break

        if board[ni - 1][nj + 1] != 'X':
            break

        cnt += 1
        ni, nj = ni - 1, nj + 1

    ni, nj = i, j
    while True:
        if not valid(ni + 1, nj - 1):
            break

        if board[ni + 1][nj - 1] != 'X':
            break

        cnt += 1
        ni, nj = ni + 1, nj - 1

    return cnt >= 4


def valid(i, j):
    return 0 <= i < 10 and 0 <= j < 10


board = []
for _ in range(10):
    board.append(list(sys.stdin.readline().strip()))

solve()
