# 백준 2869 달팽이는 올라가고 싶다

import sys

def solution(a, b, v):
    start = 0
    end = 2 * v

    while (end >= start):
        mid = (start + end) // 2

        cal = (mid * a) - ((mid-1) * b)
        if cal == v :
            print(mid)
            return

        elif cal > v :
            end = mid - 1

        else :
            start = mid + 1

    if cal < v :
        mid += 1

    print(mid)


a, b, v = map(int, sys.stdin.readline().rstrip().split(" "))
solution(a, b, v)

