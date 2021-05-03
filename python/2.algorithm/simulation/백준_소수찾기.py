import sys


def solve():
    global n, nums

    ans = 0
    for num in nums:
        if num == 1:
            continue

        is_decimal = True
        for i in range(2, (num//2) + 1):
            if num % i == 0:
                is_decimal = False
                break

        if is_decimal:
            ans += 1

    print(ans)



n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()


# 4
# 2 4 5 11
# => 3