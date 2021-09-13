import sys


def solve():
    global x, y

    cur_win_per = get_win_per(x, y)
    max_x = 2_000_000_000
    s, e = 1, max_x - x

    last_play_num = -1
    while s <= e:
        play_num = (s+e)//2

        next_win_per = get_win_per(x+play_num, y+play_num)

        if cur_win_per == next_win_per:
            s = play_num + 1
        else:
            last_play_num = play_num
            e = play_num - 1

    print(last_play_num)


def get_win_per(x, y):
    return y*100//x


x, y = map(int, sys.stdin.readline().strip().split(" "))
solve()