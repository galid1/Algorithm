import sys
from collections import deque


def solve():
    global n, k, ds

    ans = sys.maxsize

    for cnt in range(k, n+1):
        cur_selected = deque(ds[:cnt-1])

        for start in range(n-cnt+1):
            cur_selected.append(ds[start+cnt-1])

            m = sum(cur_selected) / cnt
            d = cal_d(m, cur_selected, cnt)

            ans = min(ans, d)

            cur_selected.popleft()

    print(ans)


def cal_d(m, cur_selected, cnt):
    sums = 0
    for num in cur_selected:
        sums += (num-m) ** 2

    return (sums/cnt)**0.5


n, k = map(int, sys.stdin.readline().strip().split(" "))
ds = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()