# 백준 7576 토마토

import sys
import collections

class Node:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

def tomato(matrix):
    q = collections.deque()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                q.append(Node(i,j,0))

    time = 0
    while q:
        cur = q.popleft()
        time = cur.time

        # 상
        if cur.x - 1 >= 0:
            if matrix[cur.x - 1][cur.y] == 0:
                q.append(Node(cur.x - 1, cur.y, cur.time + 1))
                matrix[cur.x - 1][cur.y] = 1
        # 하
        if cur.x + 1 <= len(matrix) - 1:
            if matrix[cur.x + 1][cur.y] == 0:
                q.append(Node(cur.x + 1, cur.y, cur.time + 1))
                matrix[cur.x + 1][cur.y] = 1
        # 좌
        if cur.y - 1 >= 0:
            if matrix[cur.x][cur.y - 1] == 0:
                q.append(Node(cur.x, cur.y - 1, cur.time + 1))
                matrix[cur.x][cur.y - 1] = 1
        # 우
        if cur.y + 1 <= len(matrix[0]) - 1:
            if matrix[cur.x][cur.y + 1] == 0:
                q.append(Node(cur.x, cur.y + 1, cur.time + 1))
                matrix[cur.x][cur.y + 1] = 1

    # 익음 확인
    # 안익은게 있다면 -1 return
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                print(-1)
                return
    # 다익었으니 time return
    print(time)

m,n = list(map(int, sys.stdin.readline().rstrip().split(" ")))
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
tomato(matrix)