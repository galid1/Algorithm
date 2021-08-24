class Solution:
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')


s = Solution()

x = 1
y = 4
print(s.hammingDistance(x, y))

