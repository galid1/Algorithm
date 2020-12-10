import sys


def solution():
    global n

    answer, idx = 0, 0

    for i in range(1, 1000000 + 1):
        if idx == n:
            break

        cur_num = str(i)
        if is_decreasing(cur_num):
            answer = i
            idx += 1

    if idx != n:
        print(-1)
    else:
        print(answer)


def is_decreasing(num):
    bef = num[0]

    for i in range(1, len(num)):
        if int(bef) <= int(num[i]):
            return False

        bef = num[i]

    return True



n = int(sys.stdin.readline())
solution()