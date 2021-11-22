import sys
from collections import Counter


def solve():
    global n, k

    ans = 0
    cur = n
    while True:
        if get_bottle_cnt(cur) <= k:
            break

        need_bottle_cnt = buy_bottle(cur)
        ans += need_bottle_cnt
        cur += need_bottle_cnt

    print(ans)


def get_bottle_cnt(num):
    return Counter(bin(num)[2:])['1']


def buy_bottle(num):
    idx = get_min_bottle_idx(num)
    return pow(2, idx)


def get_min_bottle_idx(num):
    bin_num = bin(num)

    idx = len(bin_num) - 1
    while idx >= 2:
        if bin_num[idx] == '1':
            return len(bin_num) - 1 - idx

        idx -= 1


n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()