import sys
from collections import deque


def solve():
    chain_cnt = 0
    while remove_puyo():
        chain_cnt += 1
        move_puyo()

    print(chain_cnt)


def remove_puyo():
    global board, ds

    removed = False

    for i in range(12):
        for j in range(6):
            # 빈칸
            if board[i][j] == '.':
                continue

            visited = [[False for _ in range(6)] for _ in range(12)]
            visited[i][j] = True
            q = deque([(i, j)])

            cur_color = board[i][j]
            connected_cnt = 1
            temp_puyo = []
            while q:
                cx, cy = q.popleft()
                temp_puyo.append((cx, cy))

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not is_valid(nx, ny):
                        continue

                    if visited[nx][ny]:
                        continue

                    if board[nx][ny] != cur_color:
                        continue

                    visited[nx][ny] = True
                    connected_cnt += 1
                    q.append((nx, ny))

            if connected_cnt >= 4:
                removed = True
                for x, y in temp_puyo:
                    board[x][y] = '.'

    return removed


def move_puyo():
    global board

    for j in range(6):
        puyos = []
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                puyos.append(board[i][j])
                board[i][j] = '.'

        for idx, puyo in enumerate(puyos):
            board[12-idx-1][j] = puyo


def is_valid(x, y):
    return 0 <= x < 12 and 0 <= y < 6


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
board = []
for _ in range(12):
    board.append(list(sys.stdin.readline().strip()))
solve()



# ......
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# .YY...
# .YGG..
# RRYG..
# RRYGG.


# ......
# ......
# ......
# ......
# ...GBG
# .BBBRB
# RRBGRG
# RBRGRG
# BRRGRG
# BRBBGB
# GGBRGB
# GGRGBB
