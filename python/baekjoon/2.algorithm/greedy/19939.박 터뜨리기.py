import sys


def solve():
    global n, k

    num_of_min_needs = (k * (k+1) // 2)
    if n < num_of_min_needs:
        return print(-1)

    ans = k - 1

    if (n - num_of_min_needs) % k != 0:
        ans += 1

    print(ans)


n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()