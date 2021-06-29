# baekjoon 1065번 한수

import sys

n = int(sys.stdin.readline())


def count_hansoo(n):
    count = 0
    for i in range(1, n + 1):
        if check_hansoo(i):
            count += 1

    print(count)


def check_hansoo(n):
    arr = list(map(int, list(str(n))))

    before_gap = 0
    is_set_gap = False

    for i in range(1, len(arr)):
        cur = arr[i]
        before = arr[i - 1]
        cur_gap = cur - before

        if not is_set_gap:
            before_gap = cur_gap
            is_set_gap = True
            continue

        if before_gap != cur_gap:
            return False

        before_gap = cur_gap

    return True


count_hansoo(n)
