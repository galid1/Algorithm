# 메모리 초과 오류

def dijkstra(distances, visited, weight_matrix, start_node):
    # 시작 정점 초기화
    distances[start_node] = 0
    visited[start_node] = True

    # 현재 정점을 나타내는 변수
    current_node = start_node

    # 전체 반복자 (정점 수 만큼 반복)
    for i in range(1, len(distances)):
        # 현재 거리와, 현재노드부터의 거리중 짧은것을 선택하여 거리 최신화
        for j in range(1, len(distances)):
            if j is current_node:
                continue
            elif weight_matrix[current_node][j] is not 0:
                distances[j] = min(distances[j], distances[current_node] + weight_matrix[current_node][j])

        # 다음 정점 선택(가장 거리가 짧고 방문한적이 없는 노드)
        min_distances = 11
        min_node = -1
        for k in range(1, len(distances)):
            if visited[k] is False and distances[k] < min_distances:
                min_node = k
        current_node = min_node
        visited[current_node] = True

    for j in range(1, len(distances)):
        if distances[j] is 11:
            print('INF')
            continue
        else:
            print(distances[j])

# 입력 받기
sentence1 = list(map(int, input().split(" ")))
start_node_info = int(input())

# 필요 변수 초기화
distances = [11 for i in range(0, sentence1[0]+1)]
visited = [False for i in range(0, sentence1[0]+1)]
weight_matrix = [[0 for i in range(0, sentence1[0]+1)] for i in range(0, sentence1[0]+1)]

# 간선, 거리 입력받기
for i in range(0, sentence1[1]):
    arc_info = list(map(int, input().split(" ")))
    weight_matrix[arc_info[0]][arc_info[1]] = arc_info[2]

dijkstra(distances, visited, weight_matrix, start_node_info)