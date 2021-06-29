import sys

#     *             1
#    ***            3
#   *****           5
#  *******          7
# *********         9
def solve():
    global n

    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(i+i-1):
            print('*', end='')
        print()


n = int(sys.stdin.readline().strip())
solve()