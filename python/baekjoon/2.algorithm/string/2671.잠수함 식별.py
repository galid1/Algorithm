import sys


def solve():
    global s

    is_submarine = True
    idx = 0
    while idx < len(s):
        meet = check_first_condition(s, idx)

        if meet:
            idx += 2
            continue

        meet, next_idx = check_second_condition(s, idx)

        if not meet:
            is_submarine = False
            break

        idx = next_idx

    if is_submarine:
        print("SUBMARINE")
    else:
        print("NOISE")


def check_first_condition(s, idx):
    if idx + 1 >= len(s):
        return False

    return s[idx] == '0' and s[idx + 1] == '1'


def check_second_condition(s, idx):
    if idx + 3 >= len(s):
        return False, 0

    jdx = idx

    if s[jdx] != '1':
        return False, 0
    jdx += 1

    if s[jdx] != '0' or s[jdx+1] != '0':
        return False, 0
    jdx += 2

    # 0이 나올때 까지
    while jdx < len(s):
        if s[jdx] != '0':
            break
        jdx += 1

    # 1이 존재하는지 확인
    if jdx >= len(s):
        return False, 0
    jdx += 1

    while jdx < len(s) and s[jdx] == '1':
        if jdx + 3 < len(s):
            if s[jdx] == '1' and s[jdx+1] == '0' and s[jdx+2] == '0':
                break

        jdx += 1

    return True, jdx


s = sys.stdin.readline().strip()
solve()