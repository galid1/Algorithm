class Solution:
    def maxProfit(self, prices):
        ans = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                ans += prices[i+1] - prices[i]

        return ans

s = Solution()

prices = [7,1,5,3,6,4]
# prices = [3, 3, 3, 1, 2, 4, 3, 3]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5]
print(s.maxProfit(prices))