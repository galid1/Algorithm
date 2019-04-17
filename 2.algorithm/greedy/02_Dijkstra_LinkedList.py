import sys
class Node:
    node_num = -1
    links = {}

    def __init__(self, node_num):
        self.node_num = node_num
        self.links = {}
        self.distance = 11

    def link(self, target_num, weight):
        #사전에 node_num을 키로 가지는 값이 있는지 확인 후 없으면 그냥 추가 , 있으면 값 비교후 작은것으로 최신화
        if target_num not in self.links:
            self.links[target_num] = weight
        else:
            self.links[target_num] = min(weight, self.links[target_num])

class Graph:
    node_count = -1
    start_node = -1
    nodes = [0]
    distances = []
    visited = []

    def __init__(self, node_count, start_node):
        self.node_count = node_count
        self.distances = [11 for i in range(0, node_count+1)]
        self.visited = [False for i in range(0, node_count+1)]
        self.start_node = start_node
        self.make_nodes()

    def make_nodes(self):
        for i in range(1, self.node_count+1) :
            node = Node(i)
            self.nodes.insert(i, node)

    def make_link(self, node_nums):
        self.nodes[node_nums[0]].link(node_nums[1], node_nums[2])

    def dijkstra(self):
        # 시작노드 초기화
        current_node = self.nodes[self.start_node]
        self.visited[start_node] = True
        self.distances[self.start_node] = 0

        for i in range(1, len(self.nodes)-1):
            # 거리 최신화
            for j in range(1, len(self.nodes)-1):
                # 연결되어있는지 확인시 노드안의 사전에 해당 키값이 존재하는지 파악하면 됨
                if j in current_node.links:
                    self.distances[j] = min(self.distances[j],
                                             self.distances[current_node.node_num] + current_node.links[j])

            next_node = -1
            min_distances = 11
            # 다음 노드 정하기(가장 거리가 짧은 노드)
            for k in range(1, len(self.distances)):
                if k is current_node.node_num:
                    continue
                if self.visited[k] is False:
                    if self.distances[k] < min_distances:
                        next_node = k
                        min_distances = self.distances[k]

            if next_node is -1:
                return

            if next_node > 0:
                self.visited[next_node] = True
                current_node = self.nodes[next_node]


if __name__=="__main__":
    sentence1 = list(map(int, sys.stdin.readline().strip().split(" ")))
    start_node = int(sys.stdin.readline().strip())
    arcs_info = []
    for i in range(0, sentence1[1]):
        arcs_info.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    graph = Graph(sentence1[0], start_node)
    for arc_info in arcs_info:
        graph.make_link(arc_info)

    graph.dijkstra()

    for i in range(1, len(graph.nodes)):
        if graph.distances[i] is 11:
            print("INF")
            continue
        print(graph.distances[i])