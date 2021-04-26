import sys


def solve():
    global s

    res = []
    for i in range(0, len(s)):
        sentence = ''
        for j in range(i, len(s)):
            sentence += s[j]
        res.append(sentence)

    res.sort()

    for r in res:
        print(r)

s = list(sys.stdin.readline().strip())
solve()