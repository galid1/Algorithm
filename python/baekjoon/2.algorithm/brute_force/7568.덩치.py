import sys


def solve(infos):
    result = []

    for idx, cinfo in enumerate(infos):
        rank = 1
        cx, cy = cinfo
        for jdx, info in enumerate(infos):
            if idx == jdx:
                continue

            tx, ty = info
            if cx < tx and cy < ty:
                rank += 1

        result.append(rank)

    print(*result)


n = int(sys.stdin.readline().strip())
infos = []
for i in range(n):
    infos.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve(infos)

# 5
# 7 4
# 6 5
# 5 6
# 4 7
# 4 4
