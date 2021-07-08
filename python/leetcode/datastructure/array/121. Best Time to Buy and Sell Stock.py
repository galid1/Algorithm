# O(N^2) 안됨
# def maxProfit(prices):
#     ans = 0
#
#     for i in range(len(prices)-1):
#         start = prices[i]
#         for j in range(i+1, len(prices)):
#             if start >= prices[j]:
#                 continue
#             ans = max(ans, prices[j] - start)
#
#     return ans


# O(2N)
# 각 지점별 최대값을 구해놓고, 다시 현재 값과 차이를 구해서 최대값을 찾는방법
# def maxProfit(prices):
#     maxs = [0 for _ in range(len(prices))]
#
#     cur_max = prices[len(prices)-1]
#     for i in range(len(prices)-1, -1, -1):
#         cur_max = max(cur_max, prices[i])
#         maxs[i] = cur_max
#
#     ans = 0
#
#     for i in range(len(prices)-1):
#         ans = max(ans, maxs[i] - prices[i])
#
#     return ans

def maxProfit(prices):
    profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        profit = max(profit, prices[i] - min_price)

    return profit

prices = [7,1,5,3,6,4]
maxProfit(prices)