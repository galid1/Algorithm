import sys


def solve():
    global a, b, c

    nums = list(str(a * b * c))

    cnts = {str(i): 0 for i in range(0, 10)}

    for n in nums:
        cnts[n] += 1

    for c in cnts.values():
        print(c)


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
solve()
