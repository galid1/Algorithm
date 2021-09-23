import sys
from collections import deque


def solve():
    global n, m, board

    group_size = grouping()

    visited = set()
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                continue

            # 4방향 탐색하며, key를 만들기
            cur_key_arr = set()
            for dx, dy in ds:
                nx, ny = i+dx, j+dy

                if not valid(nx, ny):
                    continue

                gid = board[nx][ny]
                if gid == 0:
                    continue
                cur_key_arr.add(str(gid))

            cur_key = sorted(cur_key_arr)
            cur_key = ''.join(cur_key_arr)

            if cur_key in visited:
                continue

            cur_sum = 0
            for key in cur_key_arr:
                cur_sum += group_size[int(key)]
            ans = max(ans, cur_sum+1)

    print(ans)


def grouping():
    global n, m, board, ds

    group_size = {}

    visited = [[False for _ in range(m)] for _ in range(n)]
    cur_gid = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue

            if visited[i][j]:
                continue

            cur_gid += 1
            size = 0

            visited[i][j] = True
            q = deque([[i, j]])
            board[i][j] = cur_gid
            while q:
                cx, cy = q.popleft()
                size += 1

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not valid(nx, ny):
                        continue

                    if visited[nx][ny]:
                        continue

                    if board[nx][ny] != 1:
                        continue

                    visited[nx][ny] = True
                    board[nx][ny] = cur_gid
                    q.append([nx, ny])

            group_size[cur_gid] = size

    return group_size


def valid(x, y):
    global n, m

    return 0 <= x < n and 0 <= y < m


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
solve()