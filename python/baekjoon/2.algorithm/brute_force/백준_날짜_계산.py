import sys

def solve():
    global e, s, m

    year = 1
    se, ss, sm = 1, 1, 1
    while se != e or ss != s or sm != m:
        se = se + 1 if se < 15 else 1
        ss = ss + 1 if ss < 28 else 1
        sm = sm + 1 if sm < 19 else 1

        year += 1

    print(year)


e, s, m = map(int, sys.stdin.readline().strip().split(" "))
solve()
