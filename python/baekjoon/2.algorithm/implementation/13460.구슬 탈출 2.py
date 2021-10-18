import sys
from collections import deque


def solve():
    global n, m, board, ds

    rx, ry, bx, by = find_bead()

    # rx, ry, bx, by
    visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = True

    q = deque([[rx, ry, bx, by]])

    ans = 0
    while q:
        ans += 1

        if ans > 10:
            return print(-1)


        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            for dx, dy in ds:
                nrx, nry = move(rx, ry, dx, dy)
                nbx, nby = move(bx, by, dx, dy)

                if visited[nrx][nry][nbx][nby]:
                    continue

                if board[nbx][nby] == 'O':
                    continue

                if board[nrx][nry] == 'O':
                    return print(ans)

                if nrx == nbx and nry == nby:
                    rd = abs(rx - nrx) + abs(ry - nry)
                    bd = abs(bx - nbx) + abs(by - nby)

                    if rd > bd:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy

                visited[nrx][nry][nbx][nby] = True
                q.append([nrx, nry, nbx, nby])

    print(-1)


def move(x, y, dx, dy):
    global board, n, m

    nx, ny = x, y
    while True:
        nx, ny = nx+dx, ny+dy

        if board[nx][ny] == '#':
            nx, ny = nx - dx, ny - dy
            break

        if board[nx][ny] == 'O':
            break

    return nx, ny


def find_bead():
    global board, n, m

    rx, ry = -1, -1
    bx, by = -1, -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    return rx, ry, bx, by


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
solve()
