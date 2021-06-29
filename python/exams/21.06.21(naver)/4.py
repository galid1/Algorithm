from collections import deque


def solution(A):
    n, m = len(A), len(A[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    nation_cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue

            nation_cnt += 1
            q = deque([(i, j)])
            visited[i][j] = True
            cur_color = A[i][j]
            while q:
                cx, cy = q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, cy+dy

                    if not valid(n, m, nx, ny):
                        continue

                    if visited[nx][ny]:
                        continue

                    if A[nx][ny] == cur_color:
                        q.append((nx, ny))
                        visited[nx][ny] = True

    return nation_cnt


def valid(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


#       00          01        02         03         04         05          06
A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]
# A = [[6, 4, 6], [6, 6, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]
# A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]

solution(A)