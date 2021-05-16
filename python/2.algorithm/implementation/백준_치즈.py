import sys
from collections import deque


def solve():
    global n, m, board, ds

    answer = 0
    will_melted_cnt = 0
    bef_melted_cnt = 0
    while True:
        found = False
        q = deque([(0, 0)])
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = True

        bef_melted_cnt = will_melted_cnt
        will_melted_cnt = 0
        while q:
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx + dx, cy + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                    continue

                if board[nx][ny] == 1:
                    visited[nx][ny] = True
                    board[nx][ny] = 0
                    will_melted_cnt += 1
                    found = True
                    continue

                visited[nx][ny] = True
                q.append((nx, ny))

        if not found:
            print(answer)
            print(bef_melted_cnt)
            break

        answer += 1


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()
