import sys


def solve():
    global a, b

    min_dif = 50
    for i in range(len(b) - len(a) + 1):
        dif = 0
        for j in range(len(a)):
            if a[j] != b[j+i]:
                dif += 1
        min_dif = min(min_dif, dif)

    print(min_dif)

a, b = sys.stdin.readline().strip().split(" ")
solve()