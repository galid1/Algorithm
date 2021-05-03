import sys

def solve():
    global s

    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return print(0)

    print(1)


s = sys.stdin.readline().strip()
solve()