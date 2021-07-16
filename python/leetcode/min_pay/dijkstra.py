import heapq

def dijkstra(graph, start):
    q = [(0, start)]
    visited = set()
    while q:
        # 가장 가까운 노드 pop & 방문처리
        node_idx = heapq.heappop(q)[1]
        visited.add(node_idx)

        # 새로 꺼낸 노드로 부터 갈 수 있는 정점거리 초기화
        for next_idx, value in enumerate(graph[node_idx]):
            # 꺼낸 노드까지의 현재 거리 + 꺼낸 노드로부터 갈수 있는 거리  vs  갈 수 있는 곳의 현재까지의 거리
            graph[start][next_idx] = min((graph[start][node_idx] + graph[node_idx][next_idx]), graph[start][next_idx])

            if next_idx not in visited:
                visited.add(next_idx)
                heapq.heappush(q, (graph[start][next_idx], next_idx))

    for g in graph:
        print(g)


graph = [
    # 0
    [999, 0, 0, 0, 0, 0, 0],
    [999, 999, 2, 5, 1, 999, 999],
    [999, 2, 999, 3, 2, 999, 999],
    [999, 5, 3, 999, 3, 1, 5],
    [999, 1, 2, 3, 999, 1, 999],
    [999, 999, 999, 1, 1, 999, 2],
    [999, 999, 999, 5, 999, 2, 999]
]
dijkstra(graph, 1)