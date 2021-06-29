# baekjoon 1012번 유기농 배추

# dfs와 같이 사용

import sys
import collections

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def search(node, matrix):
    stack = collections.deque()
    stack.append(node)
    matrix[node.x][node.y] = 0

    while stack:
        cur = stack.pop()
        
        #상
        if cur.x - 1 >= 0:
            if matrix[cur.x - 1][cur.y] == 1:
                stack.append(Node(cur.x - 1, cur.y))
                matrix[cur.x - 1][cur.y] = 0
        #하
        if cur.x + 1 < len(matrix):
            if matrix[cur.x + 1][cur.y] == 1:
                stack.append(Node(cur.x + 1, cur.y))
                matrix[cur.x + 1][cur.y] = 0
        #좌
        if cur.y - 1 >= 0:
            if matrix[cur.x][cur.y - 1] == 1:
                stack.append(Node(cur.x, cur.y - 1))
                matrix[cur.x][cur.y - 1] = 0
        #우
        if cur.y + 1 < len(matrix[0]):
            if matrix[cur.x][cur.y + 1] == 1:
                stack.append(Node(cur.x, cur.y + 1))
                matrix[cur.x][cur.y + 1] = 0

def organic_cabbage(matrix):
    queue = collections.deque()
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                queue.append(Node(i,j))

    while queue:
        cur = queue.popleft()

        if matrix[cur.x][cur.y] != 1:
            continue
        
        # dfs하며 지렁이가 갈 수 있는 곳 모두 0으로 만듬
        search(cur, matrix)
        count += 1

    print(count)

testcase = int(sys.stdin.readline())
for i in range(testcase):
    # m = 가로, n = 세로, k = 배추 수
    m, n, k = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    matrix = [[0 for i in range(m)] for i in range(n)]
    for j in range(k):
        x,y = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        matrix[y][x] = 1
    organic_cabbage(matrix)