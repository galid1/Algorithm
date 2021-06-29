import sys

# 3 4
# AAAA
# ABCA
# AAAA

# 3 3
# 111
# 212
# 222

def dfs(start):
    global board, ans, dx, dy, v
    color = board[start[0]][start[1]]
    ds = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    stack = [start]

    while stack:
        cur_x, cur_y = stack.pop()
        v[cur_x][cur_y] = True

        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if is_boundary(next_x, next_y):
                if color == board[next_x][next_y]:
                    if v[next_x][next_y]:
                        if (ds[cur_x][cur_y] + 1) - ds[next_x][next_y] >= 4:
                            ans = 'Yes'
                            return

                    if not v[next_x][next_y]:
                        stack.append((next_x, next_y))
                        ds[next_x][next_y] = ds[cur_x][cur_y] + 1


def is_boundary(next_x, next_y):
    global board
    return 0 <= next_x < len(board) and 0 <= next_y < len(board[0])


def solution():
    global n, m, board, ans, v

    for i in range(n):
        for j in range(m):
            if not v[i][j]:
                dfs((i,j))

            if ans == 'Yes':
                return


ans = "No"
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))
v = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

solution()
print(ans)