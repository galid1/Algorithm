import sys


def solve(num, cnt):
    global min_ans, max_ans

    cnt += get_odd_count(num)

    if len(num) == 1:
        max_ans = max(max_ans, cnt)
        min_ans = min(min_ans, cnt)
        return

    elif len(num) == 2:
        next_num = str(sum(map(int, list(num))))
        solve(next_num, cnt)

    else:
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                next_num = str(int(num[:i + 1]) + int(num[i + 1: j + 1]) + int(num[j + 1:]))
                solve(next_num, cnt)


def get_odd_count(num):
    result = 0
    for c in num:
        if int(c) % 2 != 0:
            result += 1

    return result


num = sys.stdin.readline().strip()
min_ans, max_ans = sys.maxsize, 0
solve(num, 0)
print(min_ans, max_ans)
