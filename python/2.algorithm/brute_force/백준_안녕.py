import sys

def solve(hp, happy, start_i):
    global n, ls, hs, ans

    for i in range(start_i, n):
        if hp - ls[i] <= 0:
            continue

        n_l, n_h = hp - ls[i], happy + hs[i]
        ans = max(ans, n_h)
        solve(n_l, n_h, i+1)


n = int(sys.stdin.readline().strip())
ls = list(map(int, sys.stdin.readline().strip().split(" ")))
hs  = list(map(int, sys.stdin.readline().strip().split(" ")))
ans = 0
solve(100, 0, 0)
print(ans)