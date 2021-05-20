import sys


def solve(n):
    length = len(n)

    for i in range(length//2+1):
        if n[i] != n[length - i - 1]:
            return print("no")

    print("yes")


while True:
    n = sys.stdin.readline().strip()

    if n == '0':
        break

    solve(n)