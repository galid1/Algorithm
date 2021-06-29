import sys
from collections import deque


def solve():
    global n, m, keys, dx, dy, board

    q = deque()
    find_entries(q)

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if is_valid(nx, ny):
                handle_point(q, nx, ny)


def is_valid(x, y):
    global board, n, m, visited
    return 0 <= x < n and 0 <= y < m and not visited[x][y]


def find_entries(q):
    global n, m, visited

    # 맨위, 맨아래
    for i in (0, n - 1):
        for j in range(m):
            if is_valid(i, j):
                handle_point(q, i, j)

    # 맨왼쪽, 맨 오른쪽
    for i in (0, m - 1):
        for j in range(n):
            if is_valid(j, i):
                handle_point(q, j, i)


def handle_point(q, x, y):
    global board, docs, visited

    target = board[x][y]

    if target == '*':
        visited[x][y] = True
        return
    elif target == '.':
        q.append((x, y))
        visited[x][y] = True
    elif target == '$':
        q.append((x, y))
        docs.append('$')
        visited[x][y] = True
    elif target.isalpha():
        # 문
        if target.isupper():
            if can_open(target):
                q.append((x, y))
                visited[x][y] = True
            else:
                save_door(target, x, y)
        # 열쇠
        else:
            q.append((x, y))
            keep_key_and_open(q, target)
            visited[x][y] = True


def save_door(door, x, y):
    global doors, visited
    if not visited[x][y]:
        doors[door].append([x, y])


def keep_key_and_open(q, key):
    global keys, doors, visited
    keys[key.upper()] = True

    # 키를 찾았으니 이전에 방문해서 열지 못한 문들을 다시 열어서 q에 넣음
    for door_x, door_y in doors[key.upper()]:
        if not visited[door_x][door_y]:
            q.append((door_x, door_y))
            visited[door_x][door_y] = True


def can_open(door):
    global keys
    return keys[door]


# 입력
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    board = []
    for i in range(n):
        board.append(list(sys.stdin.readline().strip()))

    # 열쇠와, 문 초기화
    keys = {chr(i): False for i in range(65, 91)}
    doors = {chr(i): [] for i in range(65, 91)}
    for k in list(sys.stdin.readline().strip()):
        keys[k.upper()] = True

    # 방문 배열
    visited = [[False for _ in range(m)] for _ in range(n)]

    # 방향
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 정답 문서 배열
    docs = []
    solve()
    print(len(docs))

# 1
# 5 5
# ABABA
# AabaB
# Bb$aB
# AbabB
# AABAa
# 0

# 3
# 5 17
# *****************
# .............**$*
# *B*A*P*C**X*Y*.X.
# *y*x*a*p**$*$**$*
# *****************
# cz
# 5 11
# *.*********
# *...*...*x*
# *X*.*.*.*.*
# *$*...*...*
# ***********
# 0
# 7 7
# *ABCDE*
# X.....F
# W.$$$.G
# V.$$$.H
# U.$$$.J
# T.....K
# *SQPMI*
# irony

# 1
# 6 3
# ***
# ...
# *X*
# *X*
# *$*
# ***
# x

# 1
# 2 2
# $$
# $$
# 0

# 1
# 3 3
# aaa
# a$a
# aaa
# 0

# 4 5
# 1
# *A***
# *$*a.
# **$**
# **A**
# 0
#
# 1
# 5 11
# *x*********
# *...*...*.*
# *X*.*.*.*.*
# *$*...*...*
# ***********
# 0

# 1
# 3 4
# ****
# *$A*
# ****
# a