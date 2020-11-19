import sys
from collections import deque


def solution():
    global n, m, ices, dx, dy

    answer = 0

    while is_one():
        answer += 1

        if not can_make_two():
            print(0)
            return

        zeros = [[0 for _ in range(m)] for _ in range(n)]
        v = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if ices[i][j] != 0 and v[i][j] == 0:
                    q = deque()
                    q.append((i, j))
                    v[i][j] = 1

                    while q:
                        x, y = q.popleft()
                        zero_count = 0
                        for k in range(4):
                            new_x, new_y = x + dx[k], y + dy[k]
                            if 0 <= new_x < n and 0 <= new_y < m:
                                if ices[new_x][new_y] == 0:
                                    zero_count += 1

                        zeros[x][y] = zero_count

        for i in range(n):
            for j in range(m):
                ices[i][j] = max(0, ices[i][j] - zeros[i][j])

    print(answer)


def can_make_two():
    global ices, n, m

    can_make = False
    for i in range(n):
        for j in range(m):
            if ices[i][j] != 0:
                return True

    return can_make


def is_one():
    global ices, n, m

    v = [[0 for _ in range(m)] for _ in range(n)]
    part_count = 0
    for i in range(n):
        for j in range(m):
            if ices[i][j] != 0 and v[i][j] == 0:
                part_count += 1

                if part_count > 1:
                    return False

                stack = [(i,j)]
                while stack:
                    x, y = stack.pop()

                    for k in range(4):
                        new_x, new_y = x + dx[k], y + dy[k]
                        if 0 <= new_x < n and 0 <= new_y < m:
                            if v[new_x][new_y] == 0 and ices[new_x][new_y] != 0:
                                stack.append((new_x, new_y))
                                v[new_x][new_y] = 1
    return True


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n, m = map(int, sys.stdin.readline().strip().split(" "))
ices = []
for i in range(n):
    ices.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solution()