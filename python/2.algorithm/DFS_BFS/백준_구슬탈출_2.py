import sys
from collections import deque


def solve():
    global n, m, board, visited

    rx, ry, bx, by = find_bids()
    q = deque([(rx, ry, bx, by)])

    cnt = 0
    while q:
        cnt += 1
        if cnt > 10:
            return print(-1)

        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            # 4방향
            for d in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by

                # 빨간 구슬 옮길
                while True:
                    nrx, nry = nrx+dx[d], nry+dy[d]

                    if board[nrx][nry] == '#':
                        nrx, nry = nrx-dx[d], nry-dy[d]
                        break

                    if board[nrx][nry] == 'O':
                        break

                # 파란 구슬 옮김
                while True:
                    nbx, nby = nbx+dx[d], nby+dy[d]

                    if board[nbx][nby] == '#':
                        nbx, nby = nbx-dx[d], nby-dy[d]
                        break

                    if board[nbx][nby] == 'O':
                        break

                # 파란구슬 빠짐
                if board[nbx][nby] == 'O':
                    continue

                # 빨간 구슬만 빠짐(정답)
                if board[nrx][nry] == 'O':
                    return print(cnt)

                # 겹치는 경우 처리
                if (nrx, nry) == (nbx, nby):
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx, nry = nrx-dx[d], nry-dy[d]
                    else:
                        nbx, nby = nbx-dx[d], nby-dy[d]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby))


    print(-1)


def find_bids():
    global n, m, board

    rx, ry, bx, by = 0, 0, 0, 0
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

visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
solve()