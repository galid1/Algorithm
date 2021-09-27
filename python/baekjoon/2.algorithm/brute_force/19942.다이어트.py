import sys


def solve(cur, cp, cf, cs, cv, cost, start_idx):
    global N,  ings, ans, ans_group

    if len(cur) > N:
        return

    if satisfied(cp, cf, cs, cv):
        if cost < ans:
            ans = cost
            ans_group = cur.copy()
        return

    for i in range(start_idx, N):
        cur.append(str(i+1))
        solve(cur, cp+ings[i][0], cf+ings[i][1], cs+ings[i][2], cv+ings[i][3], cost+ings[i][4], i+1)
        cur.pop()


def satisfied(cp, cf, cs, cv):
    global p, f, s, v

    return cp >= p and cf >= f and cs >= s and cv >= v




N = int(sys.stdin.readline().strip())
p, f, s, v = map(int, sys.stdin.readline().strip().split(" "))

ings = []
for _ in range(N):
    cp, cf, cs, cv, cc = map(int, sys.stdin.readline().strip().split(" "))
    ings.append([cp ,cf, cs, cv ,cc])

ans = sys.maxsize
ans_group = []
solve([], 0, 0, 0, 0, 0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
    print(' '.join(ans_group))
