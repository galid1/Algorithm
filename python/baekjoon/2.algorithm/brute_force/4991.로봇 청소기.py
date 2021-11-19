import sys
from collections import deque
from itertools import permutations


def solve():
    global w, h, board

    dusts, dust_cnt, sx, sy = init()
    maps = make_map(dusts)

    for i in range(dust_cnt + 1):
        for j in range(dust_cnt + 1):
            if maps[i][j] == -1:
                return print(-1)

    s_num = board[sx][sy]
    print(cal_min_dist(maps, s_num, dust_cnt))


def cal_min_dist(maps, s_num, dust_cnt):
    min_dist = sys.maxsize

    dusts = [i for i in range(dust_cnt + 1)]
    dusts.remove(s_num)

    perm = list(permutations(dusts))

    for nums in perm:
        f = s_num
        cur_dist = 0
        for t in nums:
            cur_dist += maps[f][t]
            f = t

        min_dist = min(min_dist, cur_dist)

    return min_dist


def make_map(dusts):
    global w, h, board, ds

    maps = [[-1 if i != j else 0 for i in range(len(dusts))] for j in range(len(dusts))]
    visited = [[False for _ in range(w)] for _ in range(h)]

    v_idx = 0
    for x, y in dusts:
        v_idx += 1

        f_num = int(board[x][y])
        visited[x][y] = v_idx
        q = deque([[x, y]])
        move_cnt = 0
        while q:
            move_cnt += 1

            for _ in range(len(q)):
                cx, cy = q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not valid(nx, ny):
                        continue

                    if visited[nx][ny] == v_idx:
                        continue

                    if board[nx][ny] == 'x':
                        continue

                    visited[nx][ny] = v_idx
                    q.append([nx, ny])

                    if type(board[nx][ny]) == int:
                        maps[f_num][board[nx][ny]] = move_cnt

    return maps



def init():
    global w, h, board, visited, ds

    dusts = []
    dust_cnt = -1
    sx, sy = -1, -1

    num = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*' or board[i][j] == 'o':
                if board[i][j] == 'o':
                    sx, sy = i, j

                board[i][j] = num
                num += 1
                dust_cnt += 1
                dusts.append([i, j])

    return dusts, dust_cnt, sx, sy


def valid(x, y):
    global w, h

    return 0 <= x < h and 0 <= y < w


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while True:
    w, h = map(int, sys.stdin.readline().strip().split(" "))
    if w == 0 or h == 0:
        break

    board = []
    for _ in range(h):
        board.append(list(sys.stdin.readline().strip()))

    solve()


# 3 3
# ***
# xox
# xx*