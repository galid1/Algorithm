#baekjoon 2178 미로 탐색
import sys
import queue
#
# class Node:
#     x = 0
#     y = 0
#     d = 0
#
#     def __init__(self, x, y, d):
#         self.x = x
#         self.y = y
#         self.d = d
#
# ## x,y 는 2보다 크거나 같고 100보다 같거나 작음의 조건이 있으므로 1,0 의 경우 처리 안함
# def search_maze(maze):
#     q = queue.Queue()
#
#     start = Node(0,0,1)
#     q.put(start)
#
#     while not q.empty():
#         cur = q.get()
#
#         #방문 했다면 다음것으로 진행
#         if maze[cur.x][cur.y] == -1:
#             continue
#
#         # 상 x - 1
#         if cur.x - 1 >= 0:
#             if maze[cur.x -1][cur.y] > 0:
#                 q.put(Node(cur.x-1,cur.y,cur.d+1))
#         # 하 x + 1
#         if cur.x + 1 <= len(maze)-1:
#             if maze[cur.x + 1][cur.y] > 0:
#                 q.put(Node(cur.x + 1, cur.y, cur.d+1))
#         # 좌 y - 1
#         if cur.y - 1 >= 0:
#             if maze[cur.x][cur.y - 1] > 0:
#                 q.put(Node(cur.x, cur.y - 1, cur.d+1))
#         # 우 y + 1
#         if cur.y + 1 <= len(maze[0])-1:
#             if maze[cur.x][cur.y + 1] > 0:
#                 q.put(Node(cur.x, cur.y + 1, cur.d+1))
#
#         # 방문 처리는 -1 로써 함
#         maze[cur.x][cur.y] = -1
#
#         if cur.x == len(maze)-1 and cur.y == len(maze[0])-1:
#             return cur.d
#
#
# x,y = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# maze = []
# for i in range(x):
#     maze.append(list(map(int, sys.stdin.readline().rstrip())))
# print(search_maze(maze))



def solution():
    #     상  하  좌  우
    dn = [-1, 1, 0, 0]
    dm = [0, 0, -1, 1]

    answer = 1
    q = queue.Queue()
    visit = [[0 for i in range(m+1)] for i in range(n+1)]

    start = [0, 0]
    q.put(start)

    while q:
        for i in range(q.qsize()):
            # cur : [n, m] 형태
            cur = q.get()

            # 정답
            if cur[0] == n-1 and cur[1] == m-1:
                return answer

            # 상, 하, 좌, 우 순으로 이동가능한 곳을 탐색
            for nj in range(4):
                next = [cur[0] + dn[nj], cur[1] + dm[nj]]

                # 이미 방문한곳이면 다음으로
                if visit[next[0]][next[1]]:
                    continue

                # 미로안의 좌표인지 확인
                if 0 <= next[0] < n and 0 <= next[1] < m:
                    # 이동 가능한 칸인지 확인
                    if maze[next[0]][next[1]] == '1':
                        visit[next[0]][next[1]] = True
                        q.put(next)

        answer += 1


n, m = map(int, sys.stdin.readline().split(" "))
maze = []
for i in range(n):
    row = list(sys.stdin.readline().strip())
    maze.append(row)

print(solution())