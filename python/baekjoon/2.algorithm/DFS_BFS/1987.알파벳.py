import sys


def solve(x, y, depth):
    global r, c, board, visited, ans, ds

    ans = max(ans, depth)

    for dx, dy in ds:
        nx, ny = x+dx, y+dy

        if not valid(nx, ny):
            continue

        if visited[ord(board[nx][ny]) - 65]:
            continue

        visited[ord(board[nx][ny]) - 65] = True
        solve(nx, ny, depth+1)
        visited[ord(board[nx][ny]) - 65] = False



def valid(x, y):
    global r, c
    return 0 <= x < r and 0 <= y < c


r, c = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

visited = [False for _ in range(26)]
visited[ord(board[0][0]) - 65] = True
ans = 1
solve(0, 0, 1)
print(ans)
