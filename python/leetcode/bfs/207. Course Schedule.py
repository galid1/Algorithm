from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        if not prerequisites:
            return True

        graph = self.make_graph(prerequisites)
        dependencies = self.make_dependencies(prerequisites)

        queue = deque(self.find_no_dependencies(dependencies))
        visited = set()
        while queue:
            cur = queue.pop()

            for link in graph[cur]:
                dependencies[link].remove(cur)

                if not dependencies[link] and link not in visited:
                    queue.append(link)

        return self.is_clear(dependencies)

    def is_clear(self, dependencies:dict):
        for v in dependencies.values():
            if v:
                return False

        return True


    def find_no_dependencies(self, dependencies:dict):
        no_dependencies = []
        for k, v in dependencies.items():
            if not v:
                no_dependencies.append(k)

        return no_dependencies

    def make_graph(self, prerequisites):
        graph = defaultdict(list)
        for f, t in prerequisites:
            graph[t].append(f)
            if f not in graph.keys():
                graph[f] = []

        return graph

    def make_dependencies(self, prerequisites):
        dependencies = defaultdict(set)
        for f, t in prerequisites:
            dependencies[f].add(t)
            if t not in dependencies.keys():
                dependencies[t] = set()

        return dependencies


s = Solution()
# numCourses = 2
# prerequisites = [[1, 0]]
# numCourses = 2
# prerequisites = [[1,0],[0,1]]
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(s.canFinish(numCourses, prerequisites))