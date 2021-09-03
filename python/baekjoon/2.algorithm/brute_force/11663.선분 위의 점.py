import sys


def solve():
    global n, m, lines, dots

    dots.sort()

    for line_start, line_end in lines:
        min_dot_idx = get_min_dot_idx(line_start, line_end)
        max_dot_idx = get_max_dot_idx(line_start, line_end)

        if min_dot_idx == -1 or max_dot_idx == -1:
            print(0)
        else:
            print(max_dot_idx - min_dot_idx + 1)



def get_min_dot_idx(ls, le):
    global dots

    s, e = 0, len(dots)-1
    min_dot_idx = len(dots)

    while s <= e:
        m = (s+e)//2

        if dots[m] == ls:
            return m
        elif ls <= dots[m] <= le:
            min_dot_idx = min(min_dot_idx, m)

        if dots[m] > ls:
            e = m-1
        elif dots[m] < ls:
            s = m+1

    if min_dot_idx == len(dots):
        return -1
    return min_dot_idx


def get_max_dot_idx(ls, le):
    global dots

    s, e = 0, len(dots)-1
    max_dot_idx = -1

    while s <= e:
        m = (s+e)//2

        if dots[m] == le:
            return m
        elif ls <= dots[m] <= le:
            max_dot_idx = max(max_dot_idx, m)

        if dots[m] > le:
            e = m-1
        elif dots[m] < le:
            s = m+1

    return max_dot_idx



n, m = map(int, sys.stdin.readline().strip().split(" "))
dots = list(map(int, sys.stdin.readline().strip().split(" ")))
lines = []
for _ in range(m):
    lines.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()