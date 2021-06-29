# baekjoon 2231 분해합

import sys


def solve(num):
    result = []

    for i in range(num + 1):
        num_list = list(map(int, list(str(i))))
        disassembly_sum = i + sum(num_list)

        if disassembly_sum == num:
            result.append(i)

    if len(result) == 0:
        return 0

    return min(result)


n = int(sys.stdin.readline())

print(solve(n))
