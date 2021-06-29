import sys


def solve():
    global n, pattern, patterns, ss

    for s in ss:
        if len(pattern) - 1 > len(s):
            print("NE")
            continue

        if matching(patterns[0], s) and matching(patterns[1], s, True):
            print("DA")
        else:
            print("NE")


def matching(pattern_word, target_word, end=False):
    length = len(pattern_word)
    target_length = len(target_word)

    if not end:
        for i in range(length):
            if pattern_word[i] != target_word[i]:
                return False
    else:
        len_diff = target_length-length
        for i in range(target_length-1, len_diff-1, -1):
            if pattern_word[i-len_diff] != target_word[i]:
                return False

    return True


n = int(sys.stdin.readline().strip())
pattern = sys.stdin.readline().strip()
patterns = pattern.split("*")
ss = []
for _ in range(n):
    ss.append(sys.stdin.readline().strip())

solve()

# 4
# asd*ccc
# asd c
# asd cc
# asd ccc
# as ccc

# 2
# aac*bbd
# aac asdac bbd
# aacbbd

# 1
# a*a
# a
