import sys
from itertools import combinations


def solve(cnt):
    global game, results, ans

    if cnt == 15:
        for result in results:
            if result != 0:
                    return
        ans = 1
        return

    t1, t2 = game[cnt]
    t1, t2 = t1 * 3, t2 * 3

    if results[t1 + 0] > 0 and results[t2 + 2] > 0:
        results[t1 + 0] -= 1
        results[t2 + 2] -= 1
        solve(cnt + 1)
        results[t1 + 0] += 1
        results[t2 + 2] += 1

    if results[t1 + 1] > 0 and results[t2 + 1] > 0:
        results[t1 + 1] -= 1
        results[t2 + 1] -= 1
        solve(cnt + 1)
        results[t1 + 1] += 1
        results[t2 + 1] += 1

    if results[t1 + 2] > 0 and results[t2 + 0] > 0:
        results[t1 + 2] -= 1
        results[t2 + 0] -= 1
        solve(cnt + 1)
        results[t1 + 2] += 1
        results[t2 + 0] += 1

game = list(combinations(range(6), 2))

for i in range(4):
    results = list(map(int, sys.stdin.readline().strip().split(" ")))
    ans = 0
    solve(0)
    print(ans, end=' ')