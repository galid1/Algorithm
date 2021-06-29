import sys

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

def solve():
    global n

    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(i+i-1):
            print('*', end='')
        print()

    for i in range(2, n+1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(i+i-1):
            print('*', end='')
        print()


n = int(sys.stdin.readline().strip())
solve()