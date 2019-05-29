#백준 2178 미로 탐색
import sys
import queue

class Node:
    x = 0
    y = 0
    d = 0

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

## x,y 는 2보다 크거나 같고 100보다 같거나 작음의 조건이 있으므로 1,0 의 경우 처리 안함
def search_maze(maze):
    q = queue.Queue()

    start = Node(0,0,1)
    q.put(start)

    while not q.empty():
        cur = q.get()
        
        #방문 했다면 다음것으로 진행
        if maze[cur.x][cur.y] == -1:
            continue
        
        # 상 x - 1
        if cur.x - 1 >= 0:
            if maze[cur.x -1][cur.y] > 0:
                q.put(Node(cur.x-1,cur.y,cur.d+1))
        # 하 x + 1
        if cur.x + 1 <= len(maze)-1:
            if maze[cur.x + 1][cur.y] > 0:
                q.put(Node(cur.x + 1, cur.y, cur.d+1))
        # 좌 y - 1
        if cur.y - 1 >= 0:
            if maze[cur.x][cur.y - 1] > 0:
                q.put(Node(cur.x, cur.y - 1, cur.d+1))
        # 우 y + 1
        if cur.y + 1 <= len(maze[0])-1:
            if maze[cur.x][cur.y + 1] > 0:
                q.put(Node(cur.x, cur.y + 1, cur.d+1))

        # 방문 처리는 -1 로써 함
        maze[cur.x][cur.y] = -1

        if cur.x == len(maze)-1 and cur.y == len(maze[0])-1:
            return cur.d


x,y = list(map(int, sys.stdin.readline().rstrip().split(" ")))
maze = []
for i in range(x):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))
print(search_maze(maze))
