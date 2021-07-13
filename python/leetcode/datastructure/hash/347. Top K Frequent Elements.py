import heapq

# dict 정렬을 이용한 풀이
# def topKFrequent(nums, k):
#     cnts = {}
#     for num in nums:
#         if num not in cnts.keys():
#             cnts[num] = 1
#         else:
#             cnts[num] += 1
#
#     cnts = dict(sorted(cnts.items(), key = lambda item: item[1], reverse=True))
#
#     ans = []
#     idx = 0
#     for key, value in cnts.items():
#         idx += 1
#         ans.append(key)
#
#         if idx == k:
#             break
#
#     return ans


def topKFrequent(nums, k):
    cnts = {}
    for num in nums:
        if num in cnts.keys():
            cnts[num] += 1
        else:
            cnts[num] = 1

    heap = []
    for key, value in cnts.items():
        heapq.heappush(heap, (-value, key))

    ans = []
    for i in range(k):
        ans.append(heapq.heappop(heap)[1])

    return ans

nums = [1,1,1,2,2,3]
# nums = [1,2]
# nums = [4,1,-1,2,-1,2,3]
k = 2
topKFrequent(nums, k)
