# 백준 3055 탈출

import sys
import collections

# 고슴도치의 위치와 물의 위치에 모두 사용
class Node:
    def __init__(self, x, y, count = 0):
        self.x = x
        self.y = y
        self.count = count

def escape(matrix):
    #     상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 처리
    visit = [[-1 for i in range(len(matrix[0]))] for i in range(len(matrix))]

    # 고슴도치를 위한 큐
    s_queue_1 = collections.deque()
    s_queue_2 = collections.deque()
    # 물 번짐을 위한 큐
    w_queue_1 = collections.deque()
    w_queue_2 = collections.deque()

    # 고슴도치, 물 시작 노드 생성
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                s_queue_1.append(Node(i, j, 0))
            if matrix[i][j] == '*':
                w_queue_1.append(Node(i, j))

    # 고슴도치가 이동 불가능할 때 까지
    while s_queue_1:
        # 물처리 (현재 턴에 이동할 수 있는 물의 위치를 모두 이동하도록 해야함)
        while w_queue_1 :
            w_cur = w_queue_1.popleft()
            for k in range(4):
                nx = w_cur.x + dx[k]
                ny = w_cur.y + dy[k]
                
                # nx, ny 가 matrix 범위 안인 경우
                if nx >= 0 and ny >= 0 and nx < len(matrix) and ny < len(matrix[0]):
                    # '.', 'S' 인 경우에만 물이 번지므로 이미 방문한 것인지 굳이 확인 안해도됨
                    if (matrix[nx][ny] == '.' or matrix[nx][ny] == 'S') and matrix[nx][ny] != 'X' and matrix[nx][ny] != 'D':
                        w_queue_2.append(Node(nx, ny))
                        matrix[nx][ny] = '*'

        w_queue_1 = w_queue_2
        w_queue_2 = collections.deque()

        # 고슴도치 이동처리
        while s_queue_1 :
            s_cur = s_queue_1.popleft()
            for g in range(4):
                nx = s_cur.x + dx[g]
                ny = s_cur.y + dy[g]

                # nx, ny 가 matrxi 범위 안인 경우
                if nx >= 0 and ny >= 0 and nx < len(matrix) and ny < len(matrix[0]):
                    # 도착 처리
                    if matrix[nx][ny] == 'D':
                        print(s_cur.count + 1)
                        return

                    # 방문처리 및 고슴도치 이동
                    if matrix[nx][ny] == '.' and matrix[nx][ny] != 'X' and visit[nx][ny] == -1:
                        s_queue_2.append(Node(nx, ny, s_cur.count + 1))
                        matrix[nx][ny] = 'S' #이동 위치를 눈으로 보기위해 일부러 추가한 코드
                        visit[nx][ny] = 1

        s_queue_1 = s_queue_2
        s_queue_2 = collections.deque()

    # 도착 불가능
    print("KAKTUS")

R, C = list(map(int, sys.stdin.readline().rstrip().split(" ")))
matrix = []
for i in range(R):
    matrix.append(list(sys.stdin.readline().rstrip()))
escape(matrix)