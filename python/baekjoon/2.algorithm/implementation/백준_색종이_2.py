import sys
from collections import deque


def solve():
    global n, positions, ds, board

    append_paper(positions)

    visited = [[False for _ in range(board_size)] for _ in range(board_size)]

    surround = 0
    for i in range(board_size):
        for j in range(board_size):
            if visited[i][j]:
                continue

            if not board[i][j]:
                continue

            q = deque([(i, j)])
            visited[i][j] = True

            while q:
                cx, cy = q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not valid(nx, ny):
                        surround += 1
                        continue

                    if visited[nx][ny]:
                        continue

                    if not board[nx][ny]:
                        surround += 1
                        continue

                    visited[nx][ny] = True
                    q.append((nx, ny))

    print(surround)


def valid(x, y):
    global board_size

    return 0 <= x < board_size and 0 <= y < board_size


def append_paper(positions):
    global board

    paper_size = 10
    for x, y in positions:
        for i in range(x, x+paper_size):
            for j in range(y, y+paper_size):
                board[i][j] = True



ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
board_size = 100
board = [[False for _ in range(board_size)] for _ in range(board_size)]
n = int(sys.stdin.readline().strip())
positions = []
for _ in range(n):
    y, x = map(int, sys.stdin.readline().strip().split(" "))
    positions.append([x, y])

solve()