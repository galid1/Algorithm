import sys

class Solution:
    def __init__(self):
        self.min_h = sys.maxsize
        self.min_h_nodes = []

    def findMinHeightTrees(self, n: int, edges):
        g = self.make_graph(n, edges)
        if n <= 1:
            return list(g.keys())

        # 리프노드들 찾기
        leaves = []
        for k in g.keys():
            if len(g[k]) == 1:
                leaves.append(k)

        while len(g.keys()) > 2:
            new_leaves = []

            # 리프노드들 삭제하며 연결된 곳에서 제거
            for leaf in leaves:
                link = g[leaf].pop()
                g[link].remove(leaf)
                g.pop(leaf)

                if len(g[link]) == 1:
                    new_leaves.append(link)

            leaves = new_leaves

        return leaves


    def make_graph(self, n, edges):
        graph = {i:set() for i in range(n)}

        for f, t in edges:
            graph[f].add(t)
            graph[t].add(f)

        return graph



# n = 4
# edges = [[1,0],[1,2],[1,3]]

n = 0
edges = []

# n = 1
# edges = []

s = Solution()
print(s.findMinHeightTrees(n, edges))
