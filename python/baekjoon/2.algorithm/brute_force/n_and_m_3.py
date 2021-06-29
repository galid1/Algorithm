# baekjoon 15651 N과 M 3

import sys

def n_and_m(n, m):
    digit = 1

    # 1부터 n 까지
    for i in range(1, n + 1):
        result = []
        result.append(i)

        recursive(n, m, digit + 1, result)


def recursive(n, m, digit, result):
    if digit > m:
        for i in result:
            print(i, end=" ")
        print()
        return

    # 1부터 n까지
    for i in range(1, n + 1):
        result.append(i)
        recursive(n, m, digit + 1, result)

        result.pop()


n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
n_and_m(n, m)