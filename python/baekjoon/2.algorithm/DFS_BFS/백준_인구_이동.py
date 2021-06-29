import sys
from collections import deque


def solve():
    global n, l, r, ps, ds

    answer = 0


    while True:
        uns = []
        visited = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                un = []
                ps_sum = 0
                un_cnt = 0
                visited[i][j] = True
                q = deque([(i, j)])
                while q:
                    cx, cy = q.popleft()
                    un.append((cx, cy))
                    ps_sum += ps[cx][cy]
                    un_cnt += 1

                    for dx, dy in ds:
                        nx, ny = cx+dx, cy+dy

                        if not is_valid(nx, ny, visited):
                            continue

                        pdif = abs(ps[cx][cy] - ps[nx][ny])
                        if l <= pdif <= r:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                if un_cnt > 1:
                    uns.append((un, ps_sum, un_cnt))

        # 정답 반환
        if not uns:
            return print(answer)

        answer += 1
        move_ps(ps, uns)


def is_valid(x, y, visited):
    if 0 <= x < n and 0 <= y < n and not visited[x][y]:
        return True
    return False


def move_ps(ps, uns):
    for un, ps_sum, un_cnt in uns:
        res_ps = ps_sum//un_cnt
        for x, y in un:
            ps[x][y] = res_ps


ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n, l, r = map(int, sys.stdin.readline().strip().split(" "))
ps = []
for i in range(n):
    ps.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()