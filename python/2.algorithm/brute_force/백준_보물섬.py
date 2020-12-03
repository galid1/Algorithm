import sys
from collections import deque


def solution():
    global max_d, n, m, board, dx, dy

    for i in range(n):
        for j in range(m):
            # 육지
            if board[i][j] == 'L':
                q = deque()
                q.append((i, j))
                visit = [[0 for _ in range(m)] for _ in range(n)]
                visit[i][j] = 1
                d = -1
                while q:
                    for _ in range(len(q)):
                        cur_x, cur_y = q.popleft()

                        for k in range(4):
                            next_x, next_y = cur_x + dx[k], cur_y + dy[k]

                            if 0 <= next_x < n and 0 <= next_y < m:
                                if not visit[next_x][next_y] and board[next_x][next_y] == 'L':
                                    q.append((next_x, next_y))
                                    visit[next_x][next_y] = 1
                    d += 1

                max_d = max(max_d, d)

    print(max_d)


max_d = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []

for i in range(n):
    board.append(list(sys.stdin.readline().strip()))

solution()
