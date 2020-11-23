import sys
from collections import deque


def solution():
    global n, k, nums

    dq = deque()

    for num in nums:
        if k > 0:
            if not dq:
                dq.append(num)
                continue

            while k > 0:
                if dq and dq[-1] < num:
                    dq.pop()
                    k -= 1
                    if k == 0:
                        dq.append(num)
                else:
                    dq.append(num)
                    break
        else:
            dq.append(num)

    if k > 0:
        for i in range(k):
            dq.pop()

    print(''.join(map(str, list(dq))))


n, k = map(int, sys.stdin.readline().strip().split(" "))
nums = list(map(int, sys.stdin.readline().strip()))
solution()