import sys


def solve(target, cur, cur_sum):
    global ans, pris

    if len(cur) > 3:
        return

    if ans:
        return

    if cur_sum > target:
        return

    if len(cur) == 3:
        if cur_sum == target:
            ans = cur.copy()
        return

    for num in pris:
        cur.append(num)
        solve(target, cur, cur_sum + num)
        cur.pop()




def make_pris():
    table = [True for _ in range(1000)]
    table[0], table[1] = False, False

    for i in range(2, int(1000**0.5) + 1):
        if not table[i]:
            continue

        mul = 2
        while i*mul < 1000:
            table[i*mul] = False
            mul += 1

    pris = []
    for idx, is_pri in enumerate(table):
        if is_pri:
            pris.append(idx)

    return pris


t = int(sys.stdin.readline().strip())
pris = make_pris()
for _ in range(t):
    ans = []
    solve(int(sys.stdin.readline().strip()), [], 0)
    if ans:
        print(*ans)
    else:
        print(0)