import sys, math


def solve():
    global n

    while True:
        if find(n):
            break
        n += 1

    print(n)


def find(num):
    num_str = str(num)

    if num < 2:
        return False

    for i in range(len(num_str)//2):
        if num_str[i] != num_str[len(num_str)-1-i]:
            return False

    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False

    return True


n = int(sys.stdin.readline().strip())
solve()