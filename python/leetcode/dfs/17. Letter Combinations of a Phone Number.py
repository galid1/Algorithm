def letterCombinations(digits):
        def dfs(cur_idx, word):
            if cur_idx >= len(digits):
                ans.append(word)
                return

            for c in dmap[digits[cur_idx]]:
                dfs(cur_idx + 1, word + c)

        dmap = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d' , 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

        ans = []
        idx = 0
        if not digits:
            return ans

        dfs(idx, '')
        return ans


print(letterCombinations(digits='2'))