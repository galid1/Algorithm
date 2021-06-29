import sys


def solve():
    global s, t

    while len(s) < len(t):
        if t[-1] == 'A':
            t.pop()
            continue

        if t[-1] == 'B':
            t.pop()
            t = t[-1::-1]

    if s == ''.join(t):
        print(1)
    else:
        print(0)



s = sys.stdin.readline().strip()
t = list(sys.stdin.readline().strip())
solve()