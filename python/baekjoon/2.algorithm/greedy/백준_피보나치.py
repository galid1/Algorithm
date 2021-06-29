import sys


# 가능한거 모두 구하게 됨..
def solve():
    global ds, num

    sums = 0
    cur_idx = len(ds) - 1
    ans = []

    while sums != num:
        if cur_idx < 0:
            break

        if sums + ds[cur_idx] > num:
            cur_idx -= 1
            continue

        sums += ds[cur_idx]
        ans.append(ds[cur_idx])
        cur_idx -= 1

    ans.sort()
    print(*ans)



def get_ds(num):
    ds = [0, 1]
    cur_idx = 1

    while True:
        cur_d = ds[cur_idx] + ds[cur_idx - 1]

        if cur_d > num:
            return ds

        ds.append(cur_d)
        cur_idx += 1


t = int(sys.stdin.readline().strip())
for _ in range(t):
    num = int(sys.stdin.readline().strip())
    ds = get_ds(num)
    solve()

# 4
# 100
# 200
# 12345
# 1003
