import sys


def solution(n):
    d = [0 for _ in range(n+1)]

    if len(stairs) > 1:
        d[1] = stairs[1]

    if len(stairs) > 2:
        d[2] = stairs[2] + stairs[1]

    for i in range(3, n+1):
        d[i] = max(stairs[i-1] + d[i-3], d[i-2]) + stairs[i]

    print(d[n])


n = int(sys.stdin.readline())
stairs = [0]
for i in range(n):
    stairs.append(int(sys.stdin.readline()))

solution(n)
