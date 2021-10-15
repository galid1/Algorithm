import sys


def solve():
    global n, m, sx, sy, k, ds, nexts

    dice = [0, 0, 0, 0, 0, 0, 0]
    cb = 6

    cx, cy = sx, sy
    for cmd in cmds:
        nx, ny = cx + ds[cmd][0], cy + ds[cmd][1]
        if not valid(nx, ny):
            continue

        cx, cy = nx, ny
        move_dice(dice, cmd)
        do_copy(cx, cy, dice)
        print(dice[1])


def move_dice(dice, cmd):
    tmp = dice[6]
    if cmd == 1:
        dice[6] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp

    elif cmd == 2:
        dice[6] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = tmp

    # 북
    elif cmd == 3:
        dice[6] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = tmp

    # 남
    elif cmd == 4:
        dice[6] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp


def do_copy(x, y, dice):
    global board

    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0


def valid(x, y):
    global n, m

    return 0 <= x < n and 0 <= y < m


n, m, sx, sy, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ds = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
cmds = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()