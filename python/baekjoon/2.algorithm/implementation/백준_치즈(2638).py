import sys
from collections import deque

def solve():
    global n, m, board, ds

    time = -1
    while True:
        time += 1

        visited = [[False for _ in range(m)] for _ in range(n)]
        meet_air = [[0 for _ in range(m)] for _ in range(n)]
        visited[0][0] = True
        will_melted = []
        q = deque([(0, 0)])

        while q:
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                    continue

                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True

                if board[nx][ny] == 1 and meet_air[nx][ny] < 2:
                    meet_air[nx][ny] += 1
                    if meet_air[nx][ny] == 2:
                        will_melted.append((nx, ny))

        if not will_melted:
            break

        melt_cheese(will_melted)

    print(time)


def melt_cheese(will_melted):
    global board

    for x, y in will_melted:
        board[x][y] = 0


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()


# 5 5
# 0 0 0 0 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 0 0 0 0