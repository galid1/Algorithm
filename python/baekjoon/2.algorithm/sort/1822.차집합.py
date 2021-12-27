import sys


def solve():
    global n, m, a, b

    for num in b:
        if num in a:
            a.remove(num)

    a = list(a)
    a.sort()
    print(len(a))
    print(*a)



# 2 5 7 11
# 4 7 9

n, m = map(int, sys.stdin.readline().strip().split(" "))
a = set(map(int, sys.stdin.readline().strip().split(" ")))
b = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()