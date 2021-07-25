import sys


def solve():
    global n, m, board, ans
    ver_ds = [(0, -1), (0, 1)]
    hor_ds = [(-1, 0), (1, 0)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    def cal_cnt(i, j):
        cur_dir = board[i][j]
        stack = [(i, j)]
        visited[i][j] = True

        while stack:
            cx, cy = stack.pop()

            ds = ver_ds if cur_dir == '-' else hor_ds

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not is_valid(nx, ny):
                    continue

                if visited[nx][ny]:
                    continue

                if board[nx][ny] == cur_dir:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue

            cal_cnt(i, j)
            ans += 1

    print(ans)


ans = 0
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))
solve()


# 4 4
# -|-|
# ----
# ----
# ----