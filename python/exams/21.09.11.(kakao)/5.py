from collections import deque
import heapq


class Node:
    def __init__(self, idx, kind):
        self.kind = kind
        self.idx = idx
        self.links = []


def solution(info, edges):
    nodes = [Node(idx, kind) for idx, kind in enumerate(info)]
    for f, t in edges:
        nodes[f].links.append(nodes[t])

    for node in nodes:
        node.links = sorted(node.links, key=lambda node: node.kind)

    root = nodes[0]
    # visited = [False for _ in range(len(info))]
    hq = [[root.kind, root]]

    cur_sheeps, cur_wolves = 1, 0
    while hq:
        kind, node = heapq.heappop(hq)
        # visited[node.idx] = True

        while node.links:
            next_node = heapq.heappop(node.links)
            if next_node.kind == 0:
                cur_sheeps += 1
            else:
                cur_wolves += 1

            if valid(cur_sheeps, cur_wolves):
                heapq.heappush(hq, [next_node.kind, next_node])


    return cur_sheeps


def valid(sheeps, wolves):
    return sheeps > wolves



info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))
