import sys


def solve():
    global s

    res = ''

    for c in s:
        if c.isdigit():
            res += c

        elif c == ' ':
            res += c

        elif c.isalpha():
            if c.isupper():
                res += chr((ord(c) - ord('A') + 13)% 26 + ord('A'))
            else:
                res += chr((ord(c) - ord('a') + 13)%26 + ord('a'))

    print(res)

s = list(sys.stdin.readline())
solve()