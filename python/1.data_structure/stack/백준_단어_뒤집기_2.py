import sys


def solve():
    global s

    stack = []
    opend = False
    res = ''

    for i in range(len(s)):
        if s[i] == '<':
            while stack:
                res += stack.pop()
            res += '<'
            opend = True

        elif not opend and s[i] == ' ':
            while stack:
                res += stack.pop()
            res += ' '

        elif s[i] == '>':
            for j in range(len(stack)):
                res += stack[j]
            stack = []
            res += '>'
            opend = False

        else:
            stack.append(s[i])

    while stack:
        res += stack.pop()

    print(res)

s = list(sys.stdin.readline().strip())
solve()