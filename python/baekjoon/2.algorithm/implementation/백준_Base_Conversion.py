import sys
from collections import deque


def solve():
    global a, b, m, a_nums

    normal_num = to_normal()

    print(*to_b_num(normal_num))


def to_normal():
    global a_nums

    normal_num = 0
    for i in range(len(a_nums)):
        unit = pow(a, i)
        normal_num += unit * a_nums[i]

    return normal_num


def to_b_num(normal_num):
    global b
    b_nums = deque()

    while normal_num >= b:
        b_nums.appendleft(normal_num%b)
        normal_num = normal_num//b

    b_nums.appendleft(normal_num)

    return b_nums



a, b = map(int, sys.stdin.readline().strip().split(" "))
m = int(sys.stdin.readline().strip())
a_nums = list(map(int, sys.stdin.readline().strip().split(" ")))
a_nums = a_nums[-1::-1]
solve()

