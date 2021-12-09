import sys
from collections import defaultdict


def solve():
    global n, infos

    infos.sort(key=lambda item: item[0])
    infos.sort(key=lambda item: item[2], reverse=True)

    cnts = defaultdict(int)
    cur_grade = 0
    results = []
    for info in infos:
        country_num, std_num, grade = info

        if cnts[country_num] >= 2:
            continue

        cur_grade += 1
        cnts[country_num] += 1
        results.append((country_num, std_num))

        if cur_grade == 3:
            break

    for result in results:
        print(*result)

n = int(sys.stdin.readline().strip())
infos = []
for _ in range(n):
    info = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    infos.append(info)

solve()
