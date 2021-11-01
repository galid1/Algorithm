import sys


def solve(cx, cy, ck):
    global r, c, k, board, visited, ds, ans

    if [cx, cy] == dest:
        if ck == k:
            ans += 1
            return

    if ck >= k:
        return

    for dx, dy in ds:
        nx, ny = cx+dx, cy+dy

        if not valid(nx, ny):
            continue

        if board[nx][ny] == 'T':
            continue

        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        solve(nx, ny, ck+1)
        visited[nx][ny] = False



def valid(x, y):
    global r, c

    return 0 <= x < r and 0 <= y < c




ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
r, c, k = map(int, sys.stdin.readline().strip().split(" "))
visited = [[False for _ in range(c)] for _ in range(r)]
visited[r-1][0] = True
dest = [0, c-1]
board = []

for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))

ans = 0
solve(r-1, 0, 1)
print(ans)

# 3 4 6
# ....
# TT..
# .T..

# 3 4 6
# ....
# .T..
# .T..

# 3 4 8
# ....
# .T..
# ....