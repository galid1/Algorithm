import sys


def solve(n, ds):
    ds.sort()

    m = len(ds)//2

    distance_mid_left = cal_distance_sum(m-1, ds)
    distance_mid = cal_distance_sum(m, ds)

    if distance_mid < distance_mid_left:
        return ds[m]
    else:
        return ds[m-1]


def cal_distance_sum(idx, ds):
    sums = 0

    for i, v in enumerate(ds):
        if idx == i:
            continue

        sums += abs(ds[idx] - v)

    return sums


n = int(sys.stdin.readline().strip())
ds = list(map(int, sys.stdin.readline().strip().split(" ")))
print(solve(n, ds))

# 4
# 5 1 7 9