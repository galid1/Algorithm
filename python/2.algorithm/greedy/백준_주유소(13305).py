import sys


def solution(ds, ps):
    next_idx = 0
    res = 0

    while next_idx < len(ps) - 1:
        cur_price = ps[next_idx]

        for j in range(next_idx+1, len(ps)):
            res += ds[j-1] * cur_price
            next_idx = j

            if cur_price > ps[j]:
                break

    print(res)



c_cnt = int(sys.stdin.readline())
ds = list(map(int, sys.stdin.readline().strip().split(" ")))
ps = list(map(int, sys.stdin.readline().strip().split(" ")))
solution(ds, ps)
