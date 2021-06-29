import sys


def solve():
    global n

    nums = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    answer = 0

    for i in range(len(n)):
        if n[i].isalpha():
            num = nums[n[i]]
            answer += num * pow(16, len(n) - i - 1)
        else:
            answer += int(n[i]) * pow(16, len(n) - i - 1)

    print(answer)


n = list(sys.stdin.readline().strip())
solve()