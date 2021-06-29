# baekjoon 2667번 단지번호 붙이기

import sys
import collections

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def search(start, matrix):
    count = 0
    stack = collections.deque()

    stack.append(start)

    while stack:
        cur = stack.pop()
        matrix[cur.x][cur.y] = 0
        count += 1

        #상
        if cur.x - 1 >= 0 :
            if matrix[cur.x - 1][cur.y] == 1:
                stack.append(Node(cur.x - 1, cur.y))
                matrix[cur.x - 1][cur.y] = 0
        #하
        if cur.x + 1 < len(matrix) :
            if matrix[cur.x + 1][cur.y] == 1:
                stack.append(Node(cur.x + 1, cur.y))
                matrix[cur.x + 1][cur.y] = 0
        #좌
        if cur.y - 1 >= 0 :
            if matrix[cur.x][cur.y - 1] == 1:
                stack.append(Node(cur.x, cur.y - 1))
                matrix[cur.x][cur.y - 1] = 0
        #우
        if cur.y + 1 < len(matrix[0]) :
            if matrix[cur.x][cur.y + 1] == 1:
                stack.append(Node(cur.x, cur.y + 1))
                matrix[cur.x][cur.y + 1] = 0

    return count

def complex_numbering(matrix):
    q = collections.deque()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                q.append(Node(i,j))

    result = []
    while q :
        cur = q.popleft()

        if matrix[cur.x][cur.y] == 0:
            continue

        result.append(search(cur, matrix))

    print(len(result))
    result.sort()
    for k in result:
        print(k)


matrix = []
n = int(sys.stdin.readline())
for i in range(n):
    matrix.append(list(map(int,list(sys.stdin.readline().rstrip()))))

complex_numbering(matrix)

