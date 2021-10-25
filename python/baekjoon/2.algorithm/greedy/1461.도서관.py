import sys


def solve():
    global n, m, ps

    ps.sort()

    neg, pos = [], []
    for p in ps:
        if p < 0:
            neg.append(abs(p))
        else:
            pos.append(p)
    neg.sort()

    groups = []
    groupy_and_append(m, neg, groups)
    groupy_and_append(m, pos, groups)

    max_num = 0
    ans = 0
    for d in groups:
        max_num = max(max_num, d)
        ans += (d*2)

    print(ans - max_num)


def groupy_and_append(m, arr, groups):
    if len(arr)%m == 0:
        for i in range(m-1, len(arr), m):
            groups.append(arr[i])
        return

    a_groups = []
    a_sums = 0
    a_idx = m-1
    while a_idx < len(arr):
        a_groups.append(arr[a_idx])
        a_sums += arr[a_idx]
        a_idx += m
    a_groups.append(arr[-1])
    a_sums += arr[-1]

    b_groups = []
    b_sums = 0
    b_idx= len(arr)%m - 1
    while b_idx < len(arr):
        b_groups.append(arr[b_idx])
        b_sums += arr[b_idx]
        b_idx += m

    if a_sums < b_sums:
        groups.extend(a_groups)
    else:
        groups.extend(b_groups)


n, m = map(int, sys.stdin.readline().strip().split(" "))
ps = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()

