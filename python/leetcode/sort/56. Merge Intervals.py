# class Solution:
#     def merge(self, intervals):
#         # 역정렬
#         intervals.sort(key=lambda item: item[1], reverse=True)
#         intervals.sort(key=lambda item: item[0], reverse=True)
#
#         # 빈 리스트 예외
#         if not intervals:
#             return []
#
#         ans = []
#         compared = intervals.pop()
#         while intervals:
#             comparator = intervals.pop()
#
#             if self.can_merge(compared, comparator):
#                 compared = self.mergeElements(compared, comparator)
#                 continue
#             else:
#                 ans.append(compared)
#                 compared = comparator
#
#         ans.append(compared)
#         return ans
#
#     def can_merge(self, compared, comparator):
#         if compared[0] == comparator[0]:
#             return True
#
#         if compared[1] >= comparator[0]:
#             return True
#
#         return False
#
#     def mergeElements(self, e1, e2):
#         return [min(e1[0], e2[0]), max(e1[1], e2[1])]
#
# s = Solution()
# intervals = [[1, 3], [1, 3], [1, 4], [1, 2], [2, 6], [8, 10], [15, 18]]
# intervals = [[1,4],[4,5]]
# print(s.merge(intervals))


class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals

        intervals.sort(key=lambda item: item[1])
        intervals.sort(key=lambda item: item[0])

        cur_idx = 0
        results = []
        while cur_idx < len(intervals):
            cur_interval = intervals[cur_idx]

            t_idx = cur_idx + 1
            while t_idx < len(intervals) and self.included(cur_interval, intervals[t_idx]):
                cur_interval = self.do_merge(cur_interval, intervals[t_idx])
                t_idx += 1

            results.append(cur_interval)
            cur_idx = t_idx

        return results

    def included(self, interval_1, interval_2):
        return interval_1[1] >= interval_2[0]

    def do_merge(self, interval_1, interval_2):
        return [(interval_1[0]), max(interval_1[1], interval_2[1])]



# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[3,3],[3,3],[3,10],[15,18]]
intervals = [[1, 4], [2, 3]]
s = Solution()
print(s.merge(intervals))