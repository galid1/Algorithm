import sys


def solve():
    global n, k

    cnt = 0
    cur_div = 0

    while cnt < k and cur_div <= n:
        cur_div += 1

        if n % cur_div == 0:
            cnt += 1

    if cnt == k:
        print(cur_div)
    else:
        print(0)




n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()