import sys
from collections import defaultdict

def solve():
    global n, words

    dicts = defaultdict(int)

    for word in words:
        dicts[word] += 1

    ans = []
    max_cnt = 0

    for word, cnt in dicts.items():
        if cnt > max_cnt:
            max_cnt = cnt
            ans = [word]
        elif cnt == max_cnt:
            ans.append(word)

    ans.sort()
    print(ans[0])


n = int(sys.stdin.readline().strip())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())
solve()
# 10
# top
# top
# top
# asd
# asd
# asd
# ccc
# cc
# cc
# cc