class Solution:
    def __init__(self):
        self.ans = []
        self.maps = {}
        self.visited = {}
        self.ticket_cnt = 0

    def findItinerary(self, tickets):
        def dfs(cur, path):
            if self.ans:
                return

            if len(path) == self.ticket_cnt + 1:
                self.ans = path.copy()
                return

            for idx, next in enumerate(self.maps[cur]):
                if self.visited[cur][idx]:
                    continue

                path.append(next)
                self.visited[cur][idx] = True
                dfs(next, path)
                self.visited[cur][idx] = False
                path.pop()

        # sorted map
        self.create_maps(tickets)
        self.create_visited()
        dfs("JFK", ["JFK"])

        return self.ans

    def create_maps(self, tickets):
        maps = {}
        ticket_cnt = 0

        for f, t in tickets:
            ticket_cnt += 1

            if f not in maps.keys():
                maps[f] = [t]
            else:
                maps[f].append(t)

            if t not in maps.keys():
                maps[t] = []

        for k in maps.keys():
            maps[k].sort()

        self.ticket_cnt = ticket_cnt
        self.maps = maps


    def create_visited(self):
        for k, v in self.maps.items():
            self.visited[k] = [False for _ in range(len(v))]


# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK", "A"], ["JFK", "B"],  ["JFK", "C"], ["A", "JFK"], ["A", "JFK"], ["B", "JFK"], ["C", "A"]]
s = Solution()
print(s.findItinerary(tickets))