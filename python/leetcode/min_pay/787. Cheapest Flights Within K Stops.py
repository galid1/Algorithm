import sys, heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = self.make_graph(n, flights)

        # 정답 배열
        dist = {i:sys.maxsize for i in range(n)}
        visited = [[False for _ in range(k+1)] for _ in range(n)]

        #    p    i   k
        q = [(0, src, 0)]

        while q:
            cp, ci, ck = heapq.heappop(q)
            # 정답
            if ci == dst:
                return cp
            # 방문 검사 & 처리
            if ck < k:
                if visited[ci][ck]:
                    continue
                visited[ci][ck] = True

            for ni, np in graph[ci]:
                new_price = cp + np
                dist[ni] = min(dist[ni], cp+np)

                if ck <= k:
                    heapq.heappush(q, (new_price, ni, ck+1))

        return -1

    def make_graph(self, n, flights):
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        return graph

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0

# n = 4
# flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
# src = 0
# dst = 3
# k = 1

n = 5
flights = [[0,1,1], [0,4,2], [1,2,1], [4,2,1], [1,3,3], [2,3,1]]
src = 0
dst = 3
k = 2

s = Solution()
print(s.findCheapestPrice(n, flights, src, dst, k))
