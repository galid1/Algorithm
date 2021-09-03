import sys
from collections import deque
from itertools import permutations


def solve():
    global ans

    # 쌓을 순서 정하기
    for order in list(permutations([0, 1, 2, 3, 4], 5)):
        if ans == 12:
            return

        stacked = get_stacked(order)
        rotate_board(stacked, 0)


def get_stacked(order):
    global boards
    stacked = []

    for z in order:
        stacked.append(boards[z])

    return stacked


def rotate_board(stacked, board_idx):
    global boards

    def rotate(board_idx):
        tmp = []
        for row in stacked[board_idx]:
            tmp.append(row.copy())

        for i in range(5):
            for j in range(5):
                stacked[board_idx][j][4-i] = tmp[i][j]

    if board_idx == 5:
        for start, end in start_ends:
            if not valid_start_end(start, end, stacked):
                continue
            bfs(stacked, start, end)
        return

    for _ in range(4):
        rotate(board_idx)
        rotate_board(stacked, board_idx+1)


def valid_start_end(start, end, stacked):
    return stacked[start[0]][start[1]][start[2]] == 1 and stacked[end[0]][end[1]][end[2]] == 1


def bfs(stacked, start, end):
    global visited, visited_num, ans

    def is_end(cz, cx, cy):
        return cz == end[0] and cx == end[1] and cy == end[2]

    def valid_coor(z, x, y):
        return 0 <= z < 5 and 0 <= x < 5 and 0 <= y < 5

    visited_num += 1
    sz, sx, sy = start
    visited[sz][sx][sy] = visited_num

    q = deque([[sz, sx, sy]])

    path_cnt = -1
    while q:
        path_cnt += 1

        for _ in range(len(q)):
            cz, cx, cy = q.popleft()

            if path_cnt >= ans:
                return

            if is_end(cz, cx, cy):
                ans = min(ans, path_cnt)
                return

            for dz, dx, dy in ds:
                nz, nx, ny = cz+dz, cx+dx, cy+dy

                if not valid_coor(nz, nx, ny):
                    continue

                if visited[nz][nx][ny] == visited_num:
                    continue

                if stacked[nz][nx][ny] == 0:
                    continue

                visited[nz][nx][ny] = visited_num
                q.append([nz, nx, ny])


# 추가정보
# z, x, y
ds = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]
visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
visited_num = 0
start_ends = [[[0,0,0], [4,4,4]], [[0,0,4], [4,4,0]], [[0,4,0], [4,0,4]], [[0,4,4], [4,0,0]]]

# 입력
boards = []
for _ in range(5):
    board = []
    for _ in range(5):
        board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
    boards.append(board)

ans = sys.maxsize
solve()

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)


# 1 1 1 1 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 2 2 2 2 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 3 3 3 3 3
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 4 4 4 4 4
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 5 5 5 5 5
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0