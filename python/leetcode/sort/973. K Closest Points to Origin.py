import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            distance = pow(pow(x, 2) + pow(y, 2), 1/2)
            heapq.heappush(heap, [distance, [x,y]])

        results = []
        for _ in range(k):
            results.append(heapq.heappop(heap)[1])

        return results


s = Solution()
# points = [[1,3],[-2,2]]
points = [[3,3], [5,-1], [-2,4]]
k = 2
s.kClosest(points, k)