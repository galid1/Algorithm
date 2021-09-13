import sys


def solve():
    global n, m, ts

    s, e = 1, pow(1_000_000_000, 2)

    last_time = -1
    while s <= e:
        time = (s+e)//2

        if get_can_evaluate_person_num(ts, time) >= m:
            last_time = time
            e = time-1
        else:
            s = time+1

    print(last_time)


def get_can_evaluate_person_num(ts, time):
    num = 0
    for t in ts:
        num += time//t

    return num


n, m = map(int, sys.stdin.readline().strip().split(" "))
ts = []
for _ in range(n):
    ts.append(int(sys.stdin.readline().strip()))

solve()