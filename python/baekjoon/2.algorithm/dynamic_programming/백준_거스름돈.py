import sys

# 수학적
# def solve():
#     global n
#
#     if n == 1 or n == 3:
#         return print(-1)
#
#     five = n//5
#     remain = n%5
#
#     if remain%2 == 0:
#         return print(five + remain//2)
#     else:
#         five -= 1
#         remain += 5
#         return print(five + remain//2)
#
#
# n = int(sys.stdin.readline().strip())
# solve()


def solve(n):
    d = [0 for _ in range(100001)]
    d[1] = 100001
    d[2] = 1
    d[3] = 100001
    d[4] = 2

    for i in range(5, n+1):
        d[i] = min(d[i-2]+1, d[i-5]+1)

    if d[n] == 100001:
        return print(-1)
    print(d[n])

solve(int(sys.stdin.readline().strip()))