import sys


def solve():
    global a, b

    reverse = False
    if b > a:
        a, b = b, a
        reverse = True

    gcd = get_greatest_common_denominator(a, b)
    a, b = a//gcd, b//gcd

    if reverse:
        print('%d:%d' % (b, a))
    else:
        print('%d:%d' %(a, b))


def get_greatest_common_denominator(a, b):
    while True:
        if a%b != 0:
            t = a
            a = b
            b = t%b
        else:
            break

    return b



a, b = map(int, sys.stdin.readline().strip().split(":"))
solve()