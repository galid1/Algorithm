import sys


def solve():
    global num
    num_cnt = {i:0 for i in range(10)}

    answer = 0
    for n in num:
        if num_cnt[n] > 0:
            if n == 6 or n == 9:
                num_cnt[6] -= 1
                num_cnt[9] -= 1
            else:
                num_cnt[n] -= 1
        else:
            answer += 1
            for i in range(10):
                if i == 6 or i == 9:
                    num_cnt[i] += 2
                else:
                    num_cnt[i] += 1

            if n == 6 or n == 9:
                num_cnt[6] -= 1
                num_cnt[9] -= 1
            else:
                num_cnt[n] -= 1

    print(answer)


num = list(map(int, sys.stdin.readline().strip()))
solve()