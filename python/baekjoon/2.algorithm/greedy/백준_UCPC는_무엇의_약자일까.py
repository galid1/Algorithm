import sys


def solve():
    global ss

    uppers = ''
    for s in ss:
        if s.isalpha() and s.isupper():
            uppers += s

    res = ''
    for s in uppers:
        if len(res) == 0:
            if s == 'U':
                res += s
                continue

        if len(res) == 1:
            if s == 'C':
                res += s
                continue

        if len(res) == 2:
            if s == 'P':
                res += s
                continue

        if len(res) == 3:
            if s == 'C':
                res += s
                break

    if res == 'UCPC':
        print('I love UCPC')
    else:
        print('I hate UCPC')


ss = list(sys.stdin.readline().strip())
solve()


