import sys
from collections import deque


def solve(board, attacks):
    for attack_row in attacks:
        # print("==============")
        # for i in range(len(board)-1, -1, -1):
        #     print(board[i])

        break_mineral(board, attack_row-1)

        linked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        cluster = find_drop_cluster(board, linked)
        if not cluster:
            continue

        drop_cluster(board, cluster, linked)
        # print("------")
        # for i in range(len(board)-1, -1, -1):
        #     print(board[i])

    for i in range(len(board) - 1, -1, -1):
        print(''.join(board[i]))


def break_mineral(board, attack_row):
    global left_to_right

    start, end, inc = 0, len(board[0]), 1
    if not left_to_right:
        start, end = end, start
        start, end = start-1, end - 1
        inc *= -1

    left_to_right = not left_to_right

    for i in range(start, end, inc):
        if board[attack_row][i] == 'x':
            board[attack_row][i] = '.'
            return


def find_drop_cluster(board, linked):
    global ds

    lands = []
    for i in range(len(board[0])):
        if board[0][i] == 'x':
            lands.append([0, i])
            linked[0][i] = True
    queue = deque(lands)

    # marking
    while queue:
        cx, cy = queue.popleft()

        for dx, dy in ds:
            nx, ny = cx+dx, cy+dy

            if not valid(nx, ny, board):
                continue

            if linked[nx][ny]:
                continue

            if board[nx][ny] == '.':
                continue

            linked[nx][ny] = True
            queue.append([nx, ny])

    will_drop_cluster = []

    for row in range(1, len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'x' and not linked[row][col]:
                will_drop_cluster.append([row, col])

    return will_drop_cluster


def drop_cluster(board, cluster, linked):
    def get_drop_height(row, col):
        height = 0
        for j in range(row-1, -1, -1):
            height += 1

            if board[j][col] == 'x':
                if not linked[j][col]:
                    return sys.maxsize
                else:
                    return row - j - 1
        return height

    min_height = sys.maxsize
    for row, col in cluster:
        min_height = min(min_height, get_drop_height(row, col))

    # print('최소 높이 : ', min_height)

    for row, col in cluster:
        board[row][col] = '.'
        board[row - min_height][col] = 'x'


def valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0])


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
r, c = map(int, sys.stdin.readline().strip().split(" "))
board = deque()
for _ in range(r):
    board.appendleft(list(sys.stdin.readline().strip()))

left_to_right = True
t = int(sys.stdin.readline().strip())
attacks = list(map(int, sys.stdin.readline().strip().split(" ")))
solve(board, attacks)


# 5 3
# xxx
# x.x
# ..x
# x.x
# x.x
# 1
# 3

# 12 24
# ........................
# ........................
# ..........xxxxxxxxxxx...
# ..........x.........x...
# ..........x.........x...
# ..........x.........x...
# ..........x.........x...
# ..........xxxxxxxxxxx...
# ..............x.........
# ..............x.........
# ..............x.........
# ..............x.........
# 1
# 10


# 5 6
# ......
# ..xx..
# ..x...
# ..xx..
# .xxxx.
# 1
# 3

# 5 6
# ......
# ..xx..
# ..x...
# ..xx..
# .xxxx.
# 5
# 1 1 1 1 2

# 1 4
# xxx.
# 4
# 1 1 1 1


# 4 5
# xxx..
# x.xx.
# x....
# xxx.x
# 1
# 3

# 2 2
# .x
# xx
# 2
# 1 1


# 12 24
# ........................
# ........................
# ..........xxxxxxxxxxx...
# ..........x.........x...
# ..........x.........x...
# ..........x.........x...
# ..........x.........x...
# ..........xxxxxxxxxxx...
# ..............x.........
# ..............x.........
# ..............x.........
# ..............x.........
# 2
# 5 5