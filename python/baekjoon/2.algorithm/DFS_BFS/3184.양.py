import sys


def solve():
    global board, n, m, visited

    for i in range(n):
        for j in range(m):
            if board[i][j] == '#' or visited[i][j]:
                continue

            visited[i][j] = True
            sheep, wolf = 0, 0
            if board[i][j] == 'v':
                wolf += 1
            if board[i][j] == 'o':
                sheep += 1
            cal_sheep_wolves(i, j, sheep, wolf)

    print(total_sheep, total_wolves)


def cal_sheep_wolves(i, j, sheep, wolf):
    global ds, visited, total_sheep, total_wolves

    stack = [(i, j)]
    sheep, wolves = sheep, wolf

    while stack:
        cx, cy = stack.pop()

        for dx, dy in ds:
            nx, ny = cx + dx, cy + dy

            if not is_valid(nx, ny):
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True

            if board[nx][ny] == '#':
                continue
            if board[nx][ny] == 'v':
                wolves += 1
            if board[nx][ny] == 'o':
                sheep += 1

            stack.append((nx, ny))

    if sheep > wolves:
        total_sheep += sheep
    else:
        total_wolves += wolves


def is_valid(i, j):
    global n, m

    return 0 <= i < n and 0 <= j < m


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, sys.stdin.readline().strip().split(" "))
total_sheep, total_wolves = 0, 0
visited = [[False for _ in range(m)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

solve()
