import sys, copy
from collections import deque


def solve():
    global n, q, qs, board, board_size

    # 사이즈 만큼 나누기
    for cq in qs:
        x, y = 0, 0
        cur_adder = pow(2, cq)
        while x < board_size:
            turn(x, y, cq)

            if y + cur_adder >= board_size:
                x, y = x + cur_adder, 0
            else:
                y += cur_adder

        melt()

    print(get_total_ice_cnt())
    print(get_biggest_ice())


def turn(x, y, l):
    global board

    cx, cy = x, y
    for size in range(pow(2, l), 0, -2):
        tmp = board[cx][cy: cy+size]

        for i in range(size):
            board[cx][cy + size - 1 - i] = board[cx + i][cy]

        for i in range(size):
            board[cx + i][cy] = board[cx + size - 1][cy + i]

        for i in range(size):
            board[cx + size - 1][cy + i] = board[cx + size - 1 - i][cy + size - 1]

        for i in range(size):
            board[cx + i][cy + size - 1] = tmp[i]

        cx, cy = cx + 1, cy + 1


def melt():
    global n, ds, board, board_size

    new_board = copy.deepcopy(board)

    for i in range(board_size):
        for j in range(board_size):
            ice_cnt = 0
            for dx, dy in ds:
                nx, ny = i+dx, j+dy

                if not valid(nx, ny):
                    continue

                if board[nx][ny] >= 1:
                    ice_cnt += 1

            if ice_cnt < 3 and board[i][j] > 0:
                new_board[i][j] -= 1

    board = new_board


def get_total_ice_cnt():
    global board, n, board_size
    total_cnt = 0
    for i in range(board_size):
        for j in range(board_size):
            total_cnt += board[i][j]

    return total_cnt


def get_biggest_ice():
    global board, n, board_size

    visited = [[False for _ in range(board_size)] for _ in range(board_size)]

    biggest_ice_size = 0

    for i in range(board_size):
        for j in range(board_size):
            if visited[i][j] or board[i][j] <= 0:
                continue

            ice_q = deque([(i, j)])
            visited[i][j] = True
            ice_size = 1
            while ice_q:
                cx, cy = ice_q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not valid(nx, ny) or visited[nx][ny]:
                        continue

                    visited[nx][ny] = True

                    if board[nx][ny] >= 1:
                        ice_size += 1
                        ice_q.append((nx, ny))

            biggest_ice_size = max(biggest_ice_size, ice_size)

    return biggest_ice_size


def valid(x, y):
    global n

    return 0 <= x < pow(2, n) and 0 <= y < pow(2, n)


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, q = map(int, sys.stdin.readline().strip().split(" "))
board = []
board_size = pow(2, n)
for _ in range(pow(2, n)):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
qs = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()


# 3 1
# 1 2 3 4 5 6 7 8
# 9 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32
# 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48
# 49 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64
# 1

# 3 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 2
# 2