import sys
from collections import deque


def make_wall(cur, si, sj):
    global n, m, safe_area

    if len(cur) == 3:
        spread_positions = spread_virus(cur)
        safe_area = max(safe_area, get_safe_area())
        unspread_virus(spread_positions)
        return

    i, j = si, sj
    while i < n:
        if j+1 == m:
            i += 1
            j = 0
        else:
            j += 1

        if i == n:
            break

        if board[i][j] != 0:
            continue

        cur.append([i, j])
        make_wall(cur, i, j)
        cur.pop()


def spread_virus(walls):
    global board, viruses, ds, n, m

    def valid(x, y):
        return 0 <= x < n and 0 <= y < m

    q = deque(viruses)

    visited = [[False for _ in range(m)] for _ in range(n)]

    spread_positions = []
    while q:
        cx, cy = q.popleft()

        for dx, dy in ds:
            nx, ny = cx+dx, cy+dy

            if not valid(nx, ny):
                continue

            if board[nx][ny] != 0:
                continue

            if [nx, ny] in walls:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            spread_positions.append([nx, ny])
            board[nx][ny] = 2
            q.append([nx, ny])

    return spread_positions


def unspread_virus(spread_positions):
    global board

    for px, py in spread_positions:
        board[px][py] = 0


def find_virus(n, m, board):
    viruses = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                viruses.append([i, j])

    return viruses


def get_safe_area():
    global board, n, m

    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                result += 1

    return result


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

viruses = find_virus(n, m, board)

safe_area = 0
make_wall([], 0, -1)

if safe_area <= 3:
    print(0)
else:
    print(safe_area-3)
