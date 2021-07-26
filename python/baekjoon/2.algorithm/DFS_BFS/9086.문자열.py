import sys

def solve(s):
    if not s:
        return print('')

    print(s[0], end='')
    print(s[-1])


t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve(sys.stdin.readline().strip())

# 3
# ACDKJFOWIEGHE
# O
# AB