import sys

def solve(n, tips):
    tips.sort(reverse=True)

    sums = 0
    for i, tip in enumerate(tips):
        receiving = tip-i

        if receiving <= 0:
            continue

        sums += receiving

    print(sums)


n = int(sys.stdin.readline().strip())
tips = []
for _ in range(n):
    tips.append(int(sys.stdin.readline().strip()))

solve(n, tips)

