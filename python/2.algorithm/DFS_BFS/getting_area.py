# 백준 2583 영역 구하기

import sys, collections

def paint_rectangle(grid_paper, rectangle_area_info):
    for info in rectangle_area_info:
        for i in range(info[1], info[3]):
            for j in range(info[0], info[2]):
                grid_paper[i][j] = 1

class Node :
    def __init__(self, x, y):
        self.x = x
        self.y = y

def cal_area(grid_paper, getting_area):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x in range(len(grid_paper)):
        for y in range(len(grid_paper[0])):
            if grid_paper[x][y] != 1 :
                area_size = 1
                queue = collections.deque()
                queue.append(Node(x, y))
                grid_paper[x][y] = 1

                while queue :
                    cur = queue.popleft()

                    for i in range(4):
                        new_x = cur.x + dx[i]
                        new_y = cur.y + dy[i]
                        # 상,하,좌,우 이동했을 때, 모눈종이의 범위에 해당하고, 1이 아닌 경우 다음을 행함 => 영역 크기 + 1 , 큐에 해당 노드 넣기, 방문 처리(1)
                        if new_x >= 0 and new_x < len(grid_paper) \
                            and new_y >= 0 and new_y < len(grid_paper[0]) :
                                if grid_paper[new_x][new_y] != 1 :
                                    area_size += 1
                                    queue.append(Node(new_x, new_y))
                                    grid_paper[new_x][new_y] = 1

                getting_area.append(area_size)


def solution(m, n, rectangle_area_info):
    grid_paper = [[0 for i in range(n)] for i in range(m)]
    getting_area = []

    # 사각형 영역 표시
    paint_rectangle(grid_paper, rectangle_area_info)

    # 빈 영역 구하기
    cal_area(grid_paper, getting_area)

    # 결과
    getting_area.sort()
    print(len(getting_area))
    for area in getting_area :
        print(area, end=" ")


m, n, k = map(int, sys.stdin.readline().rstrip().split(" "))
area_info = []
for i in range(k):
    area_info.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

solution(m, n, area_info)
