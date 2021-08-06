import sys


def solve():
    min_b, max_b = 1, 1000000000
    ans = 1000000000

    while max_b >= min_b:
        blue_ray = (min_b + max_b) // 2

        if can_take(blue_ray):
            ans = min(ans, blue_ray)
            max_b = blue_ray - 1
        else:
            min_b = blue_ray + 1

    print(ans)

def can_take(blue_ray_size):
    global n, m, ns

    idx = 0
    for _ in range(m):
        cur_size = 0

        while True:
            if idx >= n:
                break
            if cur_size + ns[idx] > blue_ray_size:
                break

            cur_size += ns[idx]
            idx += 1

    if idx < n:
        return False
    return True


n, m = map(int, sys.stdin.readline().strip().split(" "))
ns = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()
