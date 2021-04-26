import sys

def solve():
    global s

    print(int(s[0]+s[1]) + int(s[2]+s[3]))


s = list(sys.stdin.readline().strip().split(" "))
solve()