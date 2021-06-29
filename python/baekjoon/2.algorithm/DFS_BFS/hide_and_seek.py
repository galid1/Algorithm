#baekjoon 1697 숨바꼭질
import sys
import queue

class Node:
    value = 0
    count = 0
    
    def __init__(self, value, count):
        self.value = value
        self.count = count

def hide_and_seek(n,m):
    visit = [0 for i in range(100001)]
    q = queue.Queue()
    
    start = Node(n,0)
    q.put(start)
    
    while not q.empty():
        cur = q.get()

        if cur.value == m:
            return cur.count
        
        # 이미 방분
        if visit[cur.value] == -1:
            continue

        # 조건에 따라 큐에 삽입(다음 수)
        if cur.value - 1 >= 0 and visit[cur.value - 1] != -1:
            q.put(Node(cur.value - 1, cur.count + 1))
        if cur.value + 1 <= 100000 and visit[cur.value + 1] != -1:
            q.put(Node(cur.value + 1, cur.count + 1))
        if cur.value * 2 <= 100000 and visit[cur.value * 2] != -1:
            q.put(Node(cur.value * 2, cur.count + 1))

        # 방문 처리
        visit[cur.value] = -1

n, m = list(map(int, sys.stdin.readline().split(" ")))
print(hide_and_seek(n,m))