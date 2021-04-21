import sys

def solve():
    global ms

    sums = 0
    for m in ms:
        if not sums:
            sums += m
            continue

        if abs(100 - sums) > abs(100 - (sums + m)):
            sums += m
        elif abs(100 - sums) == abs(100 - (sums + m)):
            sums += m
        else:
            break

    print(sums)


ms = []
for _ in range(10):
    ms.append(int(sys.stdin.readline().strip()))

solve()