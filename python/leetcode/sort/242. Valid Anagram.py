class Solution:
    def isAnagram(self, s, t):
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()

        return s == t

s = Solution()
s1 = "anagram"
s2 = "nagaram"
s1 = "rat"
s2 = "car"
print(s.isAnagram(s1, s2))


