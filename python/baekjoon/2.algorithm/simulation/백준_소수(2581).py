import sys


def solve():
    global m, n

    min_num = sys.maxsize
    sums = 0

    for num in range(m, n+1):
        if is_decimal(num):
            min_num = min(min_num, num)
            sums += num

    if sums == 0:
        return print(-1)

    print(sums)
    print(min_num)


def is_decimal(num):
    if num == 1:
        return False

    for i in range(2, num//2 + 1):
        if num%i == 0:
            return False

    return True


m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
solve()
