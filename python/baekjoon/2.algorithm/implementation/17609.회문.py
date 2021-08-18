import sys
sys.setrecursionlimit(100000)


def solve(n, ss):
    for s in ss:
        print(decide_palindrome(s, 0, len(s)-1, False))


def decide_palindrome(s, L, R, skip=False):
    if L >= R:
        if skip:
            return 1
        else:
            return 0

    if s[L] == s[R]:
        return decide_palindrome(s, L+1, R-1, skip)
    else:
        if not skip:
            a = decide_palindrome(s, L+1, R, True)
            b = decide_palindrome(s, L, R-1, True)
            return min(a, b)
        else:
            return 2


n = int(sys.stdin.readline().strip())
ss = []
for _ in range(n):
    ss.append(sys.stdin.readline().strip())

solve(n, ss)


# 5
# zaa
# zaba
# azba
# aba
# abab


# 3
# abba
# abcba
# abbba


# 5
# abcbba
# adbbdd
# ddddd
# d
# dd


