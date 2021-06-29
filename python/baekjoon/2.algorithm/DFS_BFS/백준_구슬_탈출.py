import sys
from collections import deque

# 겹쳤을 때 둘중 하나를 이전 칸으로 옮기면 된다!
# abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by)
# 위 공식이 더 큰쪽이 더 많이 이동한 것으로 ! 이동방향에서 더 뒤쳐져 있던 친구다 !


def solution():
    global board, r, b, o, dx, dy, n, m
    cnt = 0
    q = deque()
    q.append((r[0], r[1], b[0], b[1]))

    visit = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

    while q and cnt < 10:
        cnt += 1

        # q 크기만큼 반복 꺼냄
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            # 상하좌우 이동
            for _ in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by

                # 구슬을 한쪽 끝까지 굴림
                while True:
                    nrx += dx[_]
                    nry += dy[_]
                    if board[nrx][nry] == '#':
                        nrx -= dx[_]
                        nry -= dy[_]
                        break
                    if board[nrx][nry] == 'O':
                        break

                while True:
                    nbx += dx[_]
                    nby += dy[_]
                    if board[nbx][nby] == '#':
                        nbx -= dx[_]
                        nby -= dy[_]
                        break
                    if board[nbx][nby] == 'O':
                        break

                if visit[nrx][nry][nbx][nby]:
                    continue

                # 무슨 경우든, 블루가 빠지면 그냥 다음으로
                if board[nbx][nby] == 'O':
                    continue

                # 정답
                if board[nrx][nry] == 'O':
                    return 1

                # 둘이 겹친 경우 처리
                if (nrx, nry) == (nbx, nby):
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby -  by):
                        nrx -= dx[_]
                        nry -= dy[_]
                    else:
                        nbx -= dx[_]
                        nby -= dy[_]

                visit[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby))

    return 0


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))
r, b = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            r = (i, j)
        elif board[i][j] == "B":
            b = (i, j)

print(solution())
