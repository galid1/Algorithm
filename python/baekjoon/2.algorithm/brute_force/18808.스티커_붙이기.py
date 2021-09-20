import sys


def solve():
    global n, m, k, board, stickers

    for sticker in stickers:
        # 스티커 회전
        for _ in range(4):
            if valid_size(0, 0, sticker):
                if attach(sticker):
                    break

            sticker = rotate(sticker)

    # 정답 확인
    result = 0
    for b in board:
        for point in b:
            if point == 1:
                result += 1

    print(result)


def rotate(sticker):
    new_sticker = []

    for j in range(len(sticker[0])):
        new_row = []
        for i in range(len(sticker) - 1, -1, -1):
            new_row.append(sticker[i][j])
        new_sticker.append(new_row)

    return new_sticker


def attach(sticker):
    global board, n, m

    for cx in range(n):
        for cy in range(m):
            if can_attach(cx, cy, sticker):
                do_attach(cx, cy, sticker)
                return True

    return False


def do_attach(cx, cy, sticker):
    global board

    for i in range(cx, cx + len(sticker)):
        for j in range(cy, cy + len(sticker[0])):
            if sticker[i - cx][j - cy] == 1:
                board[i][j] = 1


def can_attach(sx, sy, sticker):
    global board, n, m

    if not valid_size(sx, sy, sticker):
        return False

    for x in range(sx, sx + len(sticker)):
        for y in range(sy, sy + len(sticker[0])):
            if sticker[x - sx][y - sy] and board[x][y] == 1:
                return False
    return True

def valid_x_size(sx, sticker):
    global n

    return (sx + len(sticker) - 1) < n


def valid_y_size(sy, sticker):
    global m
    return (sy + len(sticker[0]) - 1) < m


def valid_size(sx, sy, sticker):
    global n, m
    return (sx + len(sticker) - 1) < n and (sy + len(sticker[0]) - 1) < m


n, m, k = map(int, sys.stdin.readline().strip().split(" "))
board = [[0 for _ in range(m)] for _ in range(n)]

stickers = []
for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    sticker = []
    for _ in range(a):
        sticker.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    stickers.append(sticker)

solve()
