import sys
from collections import deque


def solve():
    global n, m, board, ds

    ans = 0
    while not clear():
        ans += 1
        sx, sy = find_start()

        visited = [[0 for _ in range(m)] for _ in range(n)]
        q = deque([[sx, sy]])

        while q:
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not valid(nx, ny):
                    continue

                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append([nx, ny])

                visited[nx][ny] += 1

        do_melt(visited)

    print(ans)


def do_melt(visited):
    global board, n, m

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                board[i][j] = 0


def valid(x, y):
    global n, m

    return 0 <= x < n and 0 <= y < m



def clear():
    global n, m, board

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False

    return True


def find_start():
    global n, m

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return i, j


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
solve()