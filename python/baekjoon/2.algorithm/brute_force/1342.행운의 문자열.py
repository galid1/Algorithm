import sys
from collections import Counter

def solve():
    global cnts, length, ans

    def dfs(cur_len, bef):
        global ans

        if cur_len == length:
            ans += 1
            return

        for char in cnts.keys():
            if cnts[char] == 0 or char == bef:
                continue
            cnts[char] -= 1
            dfs(cur_len + 1, char)
            cnts[char] += 1

    dfs(0, '')
    print(ans)


s = list(sys.stdin.readline().strip())
length = len(s)
cnts = Counter(s)

ans = 0
solve()