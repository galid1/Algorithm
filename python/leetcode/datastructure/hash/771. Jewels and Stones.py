# O(N^2)
# def numJewelsInStones(jewels: str, stones: str) -> int:
#     jewels = list(jewels)
#     stones = list(stones)
#
#     cnt = 0
#     for j in jewels:
#         for s in stones:
#             if j == s:
#                 cnt += 1
#
#     return cnt

from collections import Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    cnts = Counter(stones)

    ans = 0
    for jewel in list(jewels):
        if jewel in cnts.keys():
            ans += cnts[jewel]

    return ans

jewels = "aA"
stones = "aAAbbbb"
numJewelsInStones(jewels, stones)