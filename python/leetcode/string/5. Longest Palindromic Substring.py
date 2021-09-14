class Solution:
    def longestPalindrome(self, s):
        def expand(s, si, ei):
            if s[si] != s[ei]:
                return 0, si, ei

            max_len = ei - si + 1
            while si-1 >= 0 and ei+1 < len(s) and s[si-1] == s[ei+1]:
                si, ei = si-1, ei+1
                max_len = ei - si + 1

            return max_len, si, ei


        max_len = 0
        max_si, max_ei = 0, 0

        for i in range(len(s)-1):
            tmp_len, tmp_si, tmp_ei = expand(s, i, i+1)
            if tmp_len > max_len:
                max_len, max_si, max_ei = tmp_len, tmp_si, tmp_ei

            if i+2 < len(s):
                tmp_len, tmp_si, tmp_ei = expand(s, i, i+2)
                if tmp_len > max_len:
                    max_len, max_si, max_ei = tmp_len, tmp_si, tmp_ei

        return s[max_si:max_ei+1]




solution = Solution()
# s = 'babab'
s = "cbbd"
print(solution.longestPalindrome(s))
