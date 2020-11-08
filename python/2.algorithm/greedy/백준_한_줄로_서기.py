import sys


def solution():
    global n, arr
    answers = [0 for i in range(n)]

    for i in range(n):
        left = arr[i]
        cur = i+1
        idx = 0

        while left > 0:
            if answers[idx] == 0 or answers[idx] > cur:
                idx += 1
                left -= 1
            elif answers[idx] < cur:
                idx += 1

        while answers[idx] != 0:
            idx += 1

        answers[idx] = cur

    for a in answers:
        print(a, end=' ')


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split(" ")))
solution()