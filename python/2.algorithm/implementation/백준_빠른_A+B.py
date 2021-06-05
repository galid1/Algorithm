import sys


def solve(a, b):
    print(a+b)


t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    solve(a, b)