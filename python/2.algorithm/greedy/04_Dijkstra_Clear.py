def dijkstra():
    pass

# 입력 받기
sentence1 = list(map(int, input().split(" ")))
start_node_info = int(input())

# 필요 변수 초기화
distances = [11 for i in range(0, sentence1[0]+1)]
visited = [False for i in range(0, sentence1[0]+1)]

# 간선, 거리 입력받기
for i in range(0, sentence1[1]):
    arc_info = list(map(int, input().split(" ")))


dijkstra()