import sys


def solve():
    global n

    repeat_cnt = 0

    while len(n) > 1:
        repeat_cnt += 1
        n = str(sum(map(int, list(n))))

    n = int(n)
    print(repeat_cnt)
    if (n%3) == 0:
        print("YES")
    else:
        print("NO")


n = sys.stdin.readline().strip()
solve()
# 1234567
