from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                counter += Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result
    # def leastInterval(self, tasks, n):
    #     def make_cnts_queue(tasks: dict):
    #         heap = []
    #         for task, cnt in Counter(tasks).items():
    #             heapq.heappush(heap, [-cnt, task])
    #
    #         return heap
    #
    #     def operate_cooltime(cools: dict):
    #         will_removes = []
    #
    #         for task, past_time in cools.items():
    #             if past_time + 1 == n + 1:
    #                 will_removes.append(task)
    #             else:
    #                 cools[task] += 1
    #
    #         for item in will_removes:
    #             cools.pop(item)
    #
    #     def remain_cooltime(task, cools):
    #         return task in cools
    #
    #
    #     ans = 0
    #     cnts = make_cnts_queue(tasks)
    #     cools = {}
    #     while cnts:
    #         # 쿨타임 진행
    #         operate_cooltime(cools)
    #
    #         tmps = []
    #         for _ in range(len(cnts)):
    #             cnt, task = heapq.heappop(cnts)
    #             cnt *= -1
    #
    #             if not remain_cooltime(task, cools):
    #                 if cnt-1 > 0:
    #                     cools[task] = 0
    #                     heapq.heappush(cnts, [-(cnt-1), task])
    #                 break
    #             else:
    #                 tmps.append([-cnt, task])
    #         # 불가능해서 넘어갔던 task들 다시 넣어주기
    #         for tmp in tmps:
    #             heapq.heappush(cnts, tmp)
    #
    #         ans += 1
    #
    #     return ans


s = Solution()

# tasks = ['A', 'A', 'A', 'B', 'B', 'B']
tasks = ['a','a','a','b','b','c','d']
n = 2
print(s.leastInterval(tasks, n))
