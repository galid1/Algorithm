import sys


def solve():
    global f, l

    f_digit_cnt = pow(2, len(f))
    l_digit_cnt = pow(2, len(l))

    ans = get_all_cnt(f, l)

    f_digit_kms = []
    dfs(len(f), '', f_digit_kms)

    l_digit_kms = []
    if f_digit_cnt == l_digit_cnt:
        l_digit_kms = f_digit_kms
    else:
        dfs(len(l), '', l_digit_kms)

    smaller_than_f_cnt = get_smaller_cnt(f_digit_kms, int(f))
    smaller_than_l_cnt = get_smaller_cnt(l_digit_kms, int(l), False)

    ans -= smaller_than_f_cnt
    ans -= (l_digit_cnt - smaller_than_l_cnt)
    print(ans)


def get_all_cnt(f, l):
    cnt = 0
    for i in range(len(f), len(l)+1):
        cnt += pow(2, i)
    return cnt


def get_smaller_cnt(n_digit_kms, num, is_from=True):
    cnt = 0
    for kms in n_digit_kms:
        if is_from:
            if num <= kms:
                break
        else:
            if num < kms:
                break
        cnt += 1

    return cnt


def dfs(length, cur, kms):
    if len(cur) == length:
        kms.append(int(cur))
        return

    for num in ('4', '7'):
        dfs(length, cur+num, kms)


f, l = sys.stdin.readline().strip().split(" ")
solve()