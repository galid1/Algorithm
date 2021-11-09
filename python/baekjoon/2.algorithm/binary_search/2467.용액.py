import sys


def solve():
    global ls, n

    diff, pair = sys.maxsize, [0, 0]
    for i in range(n-1):
        std = ls[i]

        s, e = i+1, n-1
        while s <= e:
            m = (s+e)//2

            sums = std + ls[m]
            if sums == 0:
                return print(ls[i], ls[m])

            # 정답 갱신
            if abs(sums) < diff:
                diff = abs(sums)
                pair = [i, m]

            if sums > 0:
                e = m-1
            else:
                s = m+1

    print(ls[pair[0]], ls[pair[1]])


n = int(sys.stdin.readline().strip())
ls = list(map(int, sys.stdin.readline().strip().split(" ")))

solve()

# 8
# -100 -99 99 0 1 2 3 4 5

# 3
# 1 2 3