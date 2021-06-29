import sys


def solve():
    global x, y

    if x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    else:
        if y > 0:
            print(2)
        else:
            print(3)



x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())
solve()