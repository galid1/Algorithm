# 재귀 풀이
# import sys
# sys.setrecursionlimit(100000)
#
# def solve(n, ss):
#     for s in ss:
#         print(decide_palindrome(s, 0, len(s)-1, False))
#
#
# def decide_palindrome(s, L, R, skip=False):
#     if L >= R:
#         if skip:
#             return 1
#         else:
#             return 0
#
#     if s[L] == s[R]:
#         return decide_palindrome(s, L+1, R-1, skip)
#     else:
#         if not skip:
#             a = decide_palindrome(s, L+1, R, True)
#             b = decide_palindrome(s, L, R-1, True)
#             return min(a, b)
#         else:
#             return 2
#
#

import sys

def solve(n, ss):
    for s in ss:
        L, R = is_palindrome(s, 0, len(s) - 1)

        if L >= R:
            print(0)
        else:
            L1, R1 = is_palindrome(s, L+1, R)
            if L1 >= R1:
                print(1)
                continue

            L2, R2 = is_palindrome(s, L, R-1)
            if L2 >= R2:
                print(1)
                continue

            print(2)


def is_palindrome(s, L, R):
    while L <= R:
        if s[L] == s[R]:
            L, R = L + 1, R - 1
        else:
            break
    return L, R


n = int(sys.stdin.readline().strip())
ss = []
for _ in range(n):
    ss.append(sys.stdin.readline().strip())

solve(n, ss)




