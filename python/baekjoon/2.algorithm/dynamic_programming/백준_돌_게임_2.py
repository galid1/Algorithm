import sys

# 수학적 풀이
# def solve(n):
#     if n%2 == 0:
#         return print("SK")
#     else:
#         return print("CY")
#
# solve(int(sys.stdin.readline().strip()))


def solve(n):
    # 0 == 상근 이김 , 1 == 찬영 이김

    d = [-1 for _ in range(1001)]
    d[1] = 1
    d[2] = 0
    d[3] = 1

    for i in range(4, n+1):
        if d[i-1] == 1 or d[i-3] == 1:
            d[i] = 0
        else:
            d[i] = 1

    if d[n] == 0:
        print("SK")
    else:
        print("CY")


solve(int(sys.stdin.readline().strip()))