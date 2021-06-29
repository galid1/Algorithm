import sys


def solve():
    global s, bs

    stack = []
    b_len = len(bs)
    last_char = bs[-1]

    for c in s:
        stack.append(c)

        if c == last_char and ''.join(stack[-b_len:]) == bs:
            del stack[-b_len:]

    if stack:
        print(''.join(stack))
    else:
        print("FRULA")


s = sys.stdin.readline().strip()
bs = sys.stdin.readline().strip()
solve()
