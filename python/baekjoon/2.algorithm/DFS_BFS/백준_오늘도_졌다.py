import sys


def solve():
    global a, b

    have_ever_win = False

    a_sum, b_sum = 0, 0
    for i in range(len(a)):
        a_sum += a[i]

        if a_sum > b_sum:
            have_ever_win = True

        b_sum += b[i]

    if have_ever_win:
        print("Yes")
    else:
        print("No")


a = list(map(int, sys.stdin.readline().strip().split(" ")))
b = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()