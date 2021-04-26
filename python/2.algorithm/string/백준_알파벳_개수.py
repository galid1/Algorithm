import sys


def solve():
    global s

    cnts = [0 for i in range(26)]

    for c in s:
        cnts[ord(c) - 97] += 1

    for cnt in cnts:
        print(cnt, end=' ')


s = list(sys.stdin.readline().strip())
solve()
