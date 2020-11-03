import sys
from collections import deque


def can_escape(x, y):
    global n, m
    return x < 0 or y < 0 or x >= n or y >= m


def is_wall(x, y):
    return arr[x][y] == '#'


def solution():
    global n, m, arr, dx, dy, v

    q = deque()

    # 동전 두개 위치 찾기
    x = -1
    y = -1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'o':
                if x == -1:
                    x, y = i, j
                else:
                    q.append([x,y,i,j])
                    v[x][y][i][j] = 1

    while q:
        # 동전 두개 꺼냄
        c1_x, c1_y, c2_x, c2_y = q.popleft()

        if v[c1_x][c1_y][c2_x][c2_y] > 10:
            break

        for j in range(4):
            # 다음 동전 위치 정하기
            n_c1_x, n_c1_y, n_c2_x, n_c2_y = c1_x + dx[j], c1_y + dy[j], c2_x + dx[j], c2_y + dy[j]

            # 탈출 하는지 확인(둘중 하나)
            if can_escape(n_c1_x, n_c1_y) ^ can_escape(n_c2_x, n_c2_y):
                print(v[c1_x][c1_y][c2_x][c2_y])
                return

            # 둘다 나가면 그냥 다음으로
            if can_escape(n_c1_x, n_c1_y) and can_escape(n_c2_x, n_c2_y):
                continue

            # 둘다 벽이어도 다음으로
            if is_wall(n_c1_x, n_c1_y) and is_wall(n_c2_x, n_c2_y):
                continue

            # 둘중 하나 벽인 경우 움직이지 않도록 함
            if arr[n_c1_x][n_c1_y] == "#":
                n_c1_x, n_c1_y = c1_x, c1_y
            if arr[n_c2_x][n_c2_y] == "#":
                n_c2_x, n_c2_y = c2_x, c2_y

            # 방문한적이 없다면
            if not v[n_c1_x][n_c1_y][n_c2_x][n_c2_y]:
                v[n_c1_x][n_c1_y][n_c2_x][n_c2_y] = v[c1_x][c1_y][c2_x][c2_y] + 1
                q.append((n_c1_x, n_c1_y, n_c2_x, n_c2_y))

    print(-1)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))

# 방문기록
v = [[[[0 for i in range(m)] for i in range(n)] for i in range(m)] for i in range(n)]

solution()


