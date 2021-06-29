import sys

graph = {
    '1': ['2', '3'],
    '2': ['1', '4'],
    '3': ['1', '4', '5'],
    '4': ['2', '3'],
    '5': ['3']
}

def dfs(start):
    stack = [start]
    visit = []

    print(start)

    while stack:
        cur = stack.pop()

        visit.append(cur)
        print('cur = ' ,cur)

        for i in range(len(graph[cur]) - 1, -1, -1):
            if graph[cur][i] in visit:
                break
            else:
                stack.append(graph[cur][i])


dfs('1')
#
# # class Node:
# #     node_num = -1
# #     links = []
# #     is_visited = -1
# #
# #     def __init__(self, node_num):
# #         self.node_num = node_num
# #         self.links = [None]
# #         self.is_visited = -1
# #
# #     def link(self, node):
# #         self.links.append(node)
# #         self.sort()
# #
# #     def sort(self):
# #         for i in range(1, len(self.links) - 1):
# #             min = i
# #             for j in range(i + 1, len(self.links)):
# #                 if self.links[min].node_num > self.links[j].node_num:
# #                     min = j
# #             temp = self.links[i]
# #             self.links[i] = self.links[min]
# #             self.links[min] = temp
# #
# # class Graph:
# #     node_count = -1
# #     start_node = -1
# #     nodes = [0]
# #
# #     def __init__(self, init_infos):
# #         self.node_count = int(init_infos[0])
# #         self.start_node = int(init_infos[2])
# #         self.make_nodes()
# #
# #     def make_nodes(self):
# #         for i in range(1, self.node_count+1 , 1) :
# #             node = Node(i)
# #             self.nodes.insert(i, node)
# #
# #     def make_link(self, node_nums):
# #         self.nodes[int(node_nums[0])].link(self.nodes[int(node_nums[1])])
# #         self.nodes[int(node_nums[1])].link(self.nodes[int(node_nums[0])])
# #
# #
# # def dfs():
# #     stack = []
# #
# #     pass
# #
# # graph_init_infos = str(input()).split(" ")
# # graph = Graph(graph_init_infos)
# #
# # for i in range(0, int(graph_init_infos[1]), 1):
# #     link_infos = str(input()).split(" ")
# #     graph.make_link(link_infos)