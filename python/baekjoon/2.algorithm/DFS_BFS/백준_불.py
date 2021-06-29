import sys
from collections import deque


def solve():
    global n, m, board, dx, dy

    (sx, sy), fs = find_sanguen_and_fire()
    sq = deque([(sx, sy)])
    fq = deque(fs)

    vs = [[False for _ in range(m)] for _ in range(n)]
    vs[sx][sy] = True
    vf = [[False for _ in range(m)] for _ in range(n)]

    ans = 0
    while sq:
        ans += 1

        # 불 이동
        for _ in range(len(fq)):
            fx, fy = fq.popleft()

            for d in range(4):
                nfx, nfy = fx+dx[d], fy+dy[d]

                # 바운더리가 아님
                if not boundary(nfx, nfy):
                    continue

                if vf[nfx][nfy]:
                    continue

                # 벽
                if board[nfx][nfy] == '#':
                    continue

                # 상근이가 있는 위치, 빈칸 이동가능
                board[nfx][nfy] = '*'
                fq.append((nfx, nfy))
                vf[nfx][nfy] = True

        # 상근 이동
        for _ in range(len(sq)):
            sx, sy = sq.popleft()

            for d in range(4):
                nsx, nsy = sx+dx[d], sy+dy[d]

                # 바운더리가 아니면 탈출 가능임
                if not boundary(nsx, nsy):
                    return print(ans)

                if vs[nsx][nsy]:
                    continue

                # 벽 or 불
                if board[nsx][nsy] == '#' or board[nsx][nsy] == '*':
                    continue

                vs[nsx][nsy] = True
                sq.append((nsx, nsy))

    print("IMPOSSIBLE")


def boundary(x, y):
    global n, m

    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def find_sanguen_and_fire():
    global n, m, board

    si, sj = 0, 0
    fs = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == '@':
                si, sj = i, j
            elif board[i][j] == '*':
                fs.append((i, j))

    return (si, sj), fs


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
t = int(sys.stdin.readline().strip())
for _ in range(t):
    m, n = map(int, sys.stdin.readline().strip().split(" "))
    board = []
    for _ in range(n):
        board.append(list(sys.stdin.readline().strip()))
    solve()