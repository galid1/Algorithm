import sys


def solution(idx, inputs):
    ans = 0

    l, p, v = inputs

    mok = v // p
    ans += mok * l
    ans += v - (mok * p)

    print("Case ", idx, ': ', ans)


idx = 1
while True:
    inputs = list(map(int, sys.stdin.readline().strip().split(" ")))

    if inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0:
        break

    solution(idx, inputs)
    idx += 1