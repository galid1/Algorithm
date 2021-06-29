import sys
from collections import deque


def solution():
    set_wall([], 0)


def set_wall(walls, start_idx):
    global dx, dy, n, m, viruses, board, max_safe_area

    # 벽위치 모두 정함
    if len(walls) == 3:
        # 벽세우기
        for (wi, wj) in walls:
            board[wi][wj] = 1

        # 바이러스 전파
        vv = [[0 for _ in range(m)] for _ in range(n)]
        q = deque(viruses)

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for di in range(4):
                    new_x, new_y = x + dx[di], y + dy[di]

                    if 0 <= new_x < n and 0 <= new_y < m and not vv[new_x][new_y] and not board[new_x][new_y]:
                        vv[new_x][new_y] = 1
                        q.append((new_x, new_y))

        # 정답갱신
        safe_area = 0
        for ai in range(n):
            for aj in range(m):
                if board[ai][aj] == 0 and vv[ai][aj] == 0:
                    safe_area += 1
        max_safe_area = max(max_safe_area, safe_area)

        # 벽수거
        for (wi, wj) in walls:
            board[wi][wj] = 0

        return


    # 벽세우기
    for i in range(start_idx, n*m):
        x, y = i//m, i%m

        if board[x][y] == 0:
            walls.append((x, y))
            set_wall(walls, i+1)
            walls.pop()
            


max_safe_area = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
viruses = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
for j in range(n):
    for k in range(m):
        if board[j][k] == 2:
            viruses.append((j, k))
solution()
print(max_safe_area)