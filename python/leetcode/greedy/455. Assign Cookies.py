class Solution:
    def findContentChildren(self, g, s):
        g.sort(reverse=True)
        s.sort(reverse=True)

        ans = 0
        gi, si = 0, 0

        while si < len(s) and gi < len(g):
            if s[si] >= g[gi]:
                ans, si, gi = ans+1, si+1, gi +1
            else:
                gi += 1

        return ans


solution = Solution()
g = [1,2,3]
s = [1,1]

g = [1,2]
s = [1,2,3]

g = [1]
s = []

g = [1,2,3,4]
s = [0]
print(solution.findContentChildren(g, s))