import sys
from collections import deque


def solve():
    global n, board, ds

    islands = find_islands()
    ans = sys.maxsize

    for q in islands:
        visited = [[False for _ in range(n)] for _ in range(n)]
        for x, y in q:
            visited[x][y] = True

        found = False
        cur_ans = 0
        while q:
            for _ in range(len(q)):
                cx, cy = q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not boundary(nx, ny) or visited[nx][ny]:
                        continue

                    if board[nx][ny] == 1:
                        found = True
                        ans = min(ans, cur_ans)
                        break

                    visited[nx][ny] = True
                    q.append((nx, ny))

                if found:
                    break

            cur_ans += 1
            if found:
                break


    print(ans)



def find_islands():
    global n, board, ds

    islands = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            if board[i][j] == 1:
                island = deque([(i, j)])
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    cx, cy = q.popleft()

                    for dx, dy in ds:
                        nx, ny = cx + dx, cy + dy

                        if not boundary(nx, ny) or visited[nx][ny]:
                            continue

                        if board[nx][ny] == 1:
                            visited[nx][ny] = True
                            island.append((nx, ny))
                            q.append((nx, ny))

                islands.append(island)

    return islands


def boundary(x, y):
    global n

    if 0 <= x < n and 0 <= y < n:
        return True
    return False


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(sys.stdin.readline().strip())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()

# 5
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 1
# 0 0 0 0 1
