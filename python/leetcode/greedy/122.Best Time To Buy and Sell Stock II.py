class Solution:
    def maxProfit(self, prices):
        ans = 0
        cur = prices[0]
        max_dif = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_dif = prices[i] - cur
            else:
                ans += max_dif
                cur = prices[i]
                max_dif = 0

        if max_dif:
            ans += max_dif

        return ans


s = Solution()

# prices = [7,1,5,3,6,4]
# prices = [3, 3, 3, 1, 2, 4, 3, 3]
# prices = [7,6,4,3,1]
prices = [1,2,3,4,5]
print(s.maxProfit(prices))