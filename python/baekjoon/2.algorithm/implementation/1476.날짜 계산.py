import sys


def solve():

    y, ce, cs, cm = 1, 1, 1, 1

    while not correct(ce, cs, cm):
        y += 1
        ce, cs, cm = to_next_year(ce, cs, cm)

    print(y)


def to_next_year(ce, cs, cm):
    ne = ce+1 if ce+1 <= 15 else 1
    ns = cs+1 if cs+1 <= 28 else 1
    nm = cm+1 if cm+1 <= 19 else 1
    return ne, ns, nm


def correct(ce, cs, cm):
    global e, s, m

    return ce == e and cs == s and cm == m


e, s, m = map(int, sys.stdin.readline().strip().split(" "))
solve()