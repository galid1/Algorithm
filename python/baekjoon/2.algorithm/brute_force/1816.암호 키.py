import sys


def solve(s):
    for num in range(1000000, 1, -1):
        if s%num == 0:
            return print("NO")

    print("YES")



t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve(int(sys.stdin.readline().strip()))