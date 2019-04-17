# 백준 11403 경로찾기

import sys
import queue

def find_route(G):
    result = [[0 for i in range(len(G[0]))] for i in range(len(G))]

    for i in range(len(G[0])):
        q = queue.Queue()
        visit = [0 for i in range(len(G[0]))]
        q.put(i)

        while not q.empty():
            cur = q.get()
            # 이미 방문 했으면 다음 것으로
            if visit[cur] == 1:
                continue
            # 방문처리
            visit[cur] = 1

            for j in range(len(G[0])):
                # 탐색할 노드가 현재 꺼낸 노드와 같으면 다음 노드로 진행
                # if j == cur:
                #     continue

                # 현재 탐색 노드에서 다음 노드로의 경로가 있다면 q에 넣고 경로 있음 처리
                if G[cur][j] == 1:
                    q.put(j)
                    result[i][j] = 1

    for j in range(len(result)):
        for k in range(len(result[0])):
            print(result[j][k], end=' ')
        print()



n = int(sys.stdin.readline().rstrip())
G = []
for i in range(n):
    G.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
find_route(G)


