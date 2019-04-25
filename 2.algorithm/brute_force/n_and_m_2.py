# 백준 15650 N과 M 2

import sys


def n_and_m(n, m):
    digit = 1

    # 1부터 n 까지
    for i in range(1, n + 1):
        result = []
        visit = [0 for i in range(m + 1)]
        visit[digit] = i
        result.append(i)

        recursive(n, m, digit + 1, visit, result)


def recursive(n, m, digit, visit, result):
    if digit > m:
        for i in result:
            print(i, end=" ")
        print()
        return

    # 1부터 n까지
    for i in range(1, n + 1):
        if i in visit:
            continue

        if result[-1] > i:
            continue

        # 방문 처리 및 새로 초기화
        visit[digit] = i
        for j in range(digit + 1, m + 1):
            visit[j] = 0

        result.append(i)
        recursive(n, m, digit + 1, visit, result)

        result.pop()
        visit[digit] = 0


n, m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
n_and_m(n, m)