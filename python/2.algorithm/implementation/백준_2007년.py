import sys


def solve():
    global m, d, days

    today = 0  # MON
    tm, td = 1, 1

    while tm < m:
        if tm in (1, 3, 5, 7, 8, 10, 12):
            today += 31%7
        elif tm in (4, 6, 9, 11):
            today += 30%7
        elif tm == 2:
            today += 28%7
        tm += 1

    td = (d - td)%7
    today = (today + td)%7

    print(days[today])



days = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}
m, d = map(int, sys.stdin.readline().strip().split(" "))
solve()