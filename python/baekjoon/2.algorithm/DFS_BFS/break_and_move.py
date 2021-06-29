# baekjoon 2206 벽 부수고 이동하기

import sys
import collections

  #    y
  # x ㅁ
class Node:
    def __init__(self, x, y, count, can_break = True):
        self.x = x
        self.y = y
        self.count = count
        self.can_break = can_break

class Visit: # True로 세팅 되어있다면 방문한 것
    def __init__(self, normal_visit = False, break_visit = False):
        self.normal_visit = normal_visit
        self.break_visit = break_visit


def break_and_move(matrix, n, m):
    queue = collections.deque()
    visit = [[Visit() for i in range(1001)] for i in range(1001)]

    queue.append(Node(0, 0, 1)) #시작 = 0,0  골 = n-1, m-1 (둘다 항상 0)
    visit[0][0] = Visit(True, True)

    #     상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cur = queue.popleft()

        # 정답
        if cur.x == n-1 and cur.y == m-1:
            print(cur.count)
            return

        for i in range(4):
            nx = cur.x + dx[i]
            ny = cur.y + dy[i]

            if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]): #매트릭스 안에 해당되는 경우
                if matrix[nx][ny] == 1: # 벽
                    if cur.can_break is True:
                        if visit[nx][ny].break_visit is False:
                            queue.append(Node(nx, ny, cur.count+1, False))
                            visit[nx][ny].break_visit = True

                elif matrix[nx][ny] == 0: # 평지
                    if cur.can_break is True and visit[nx][ny].normal_visit is False:
                        queue.append(Node(nx, ny, cur.count+1))
                        visit[nx][ny].normal_visit = True

                    elif cur.can_break is False and visit[nx][ny].break_visit is False:
                        queue.append(Node(nx, ny, cur.count + 1, False))
                        visit[nx][ny].break_visit = True

    print(-1)

n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
matrix = []

for i in range(n):
    matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
break_and_move(matrix, n, m)









## 지저분
# # 상
# if cur.x - 1 >= 0:
#     if cur.can_break is True and visit[cur.x - 1][cur.y].normal_visit is False:  # 벽을 부순적이 없고 벽을 안부순 상태로 방문한적이 없다면
#         if matrix[cur.x - 1][cur.y] == 1:  # 이동하려는곳이 벽이면
#             queue.append(Node(cur.x - 1, cur.y, cur.count + 1, False))
#             visit[cur.x - 1][cur.y].break_visit = True
#         else:  # 이동하려는 곳이 평지
#             queue.append(Node(cur.x - 1, cur.y, cur.count + 1, True))
#             visit[cur.x - 1][cur.y].normal_visit = True
# 
#     else:  # 벽을 이미 부순 경우(0만 지나갈 수 있음)
#         if matrix[cur.x - 1][cur.y] == 0 and visit[cur.x - 1][cur.y].break_visit == False:  # 0이면서 벽을 부순 상태로 방문한적이 없다면
#             queue.append(Node(cur.x - 1, cur.y, cur.count + 1, cur.can_break))
#             visit[cur.x - 1][cur.y].break_visit = True
# 
# # 하
# if cur.x + 1 < len(matrix):
#     if cur.can_break is True and visit[cur.x + 1][cur.y].normal_visit is False:  # 벽을 부순적이 없고 벽을 안부순 상태로 방문한적이 없다면
#         if matrix[cur.x + 1][cur.y] == 1:  # 이동하려는곳이 벽이면
#             queue.append(Node(cur.x + 1, cur.y, cur.count + 1, False))
#             visit[cur.x + 1][cur.y].break_visit = True
#         else:  # 이동하려는 곳이 평지
#             queue.append(Node(cur.x + 1, cur.y, cur.count + 1, True))
#             visit[cur.x + 1][cur.y].normal_visit = True
# 
#     else:  # 벽을 이미 부순 경우(0만 지나갈 수 있음)
#         if matrix[cur.x + 1][cur.y] == 0 and visit[cur.x + 1][cur.y].break_visit == False:  # 0이면서 벽을 부순 상태로 방문한적이 없다면
#             queue.append(Node(cur.x + 1, cur.y, cur.count + 1, cur.can_break))
#             visit[cur.x + 1][cur.y].break_visit = True
# 
# # 좌
# if cur.y - 1 >= 0:
#     if cur.can_break is True and visit[cur.x][cur.y - 1].normal_visit is False:  # 벽을 부순적이 없고 벽을 안부순 상태로 방문한적이 없다면
#         if matrix[cur.x][cur.y - 1] == 1:  # 이동하려는곳이 벽이면
#             queue.append(Node(cur.x, cur.y - 1, cur.count + 1, False))
#             visit[cur.x][cur.y - 1].break_visit = True
#         else:  # 이동하려는 곳이 평지
#             queue.append(Node(cur.x, cur.y - 1, cur.count + 1, True))
#             visit[cur.x][cur.y - 1].normal_visit = True
# 
#     else:  # 벽을 이미 부순 경우(0만 지나갈 수 있음)
#         if matrix[cur.x][cur.y - 1] == 0 and visit[cur.x][cur.y - 1].break_visit == False:  # 0이면서 벽을 부순 상태로 방문한적이 없다면
#             queue.append(Node(cur.x, cur.y - 1, cur.count + 1, cur.can_break))
#             visit[cur.x][cur.y - 1].break_visit = True
# # 우
# if cur.y + 1 < len(matrix[0]):
#     if cur.can_break is True and visit[cur.x][cur.y + 1].normal_visit is False:  # 벽을 부순적이 없고 벽을 안부순 상태로 방문한적이 없다면
#         if matrix[cur.x][cur.y + 1] == 1:  # 이동하려는곳이 벽이면
#             queue.append(Node(cur.x, cur.y + 1, cur.count + 1, False))
#             visit[cur.x][cur.y + 1].break_visit = True
#         else:  # 이동하려는 곳이 평지
#             queue.append(Node(cur.x, cur.y + 1, cur.count + 1, True))
#             visit[cur.x][cur.y + 1].normal_visit = True
# 
#     else:  # 벽을 이미 부순 경우(0만 지나갈 수 있음)
#         if matrix[cur.x][cur.y + 1] == 0 and visit[cur.x][cur.y + 1].break_visit == False:  # 0이면서 벽을 부순 상태로 방문한적이 없다면
#             queue.append(Node(cur.x, cur.y + 1, cur.count + 1, cur.can_break))
#             visit[cur.x][cur.y + 1].break_visit = True