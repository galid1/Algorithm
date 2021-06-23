import sys


def solve(n, m):
    sums = 0
    min_num = 0

    for i in range(n, m+1):
        square_root = pow(i, 1/2)

        if square_root == int(square_root) and int(pow(square_root, 2)) == i:
            if sums == 0:
                min_num = i
            sums += i

    if sums == 0:
        print(-1)
    else:
        print(sums)
        print(min_num)



n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
solve(n, m)
