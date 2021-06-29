import sys


def solution():
    global n, s, ns, ans, changed

    l, r = 0, 0
    sums = ns[r]

    while l <= r < n:
        if sums >= s:
            ans = min(ans, r-l+1)
            changed = True
            sums -= ns[l]
            l += 1
        else:
            r += 1
            if r < n:
                sums += ns[r]

ans = sys.maxsize
changed = False
n, s = map(int, sys.stdin.readline().strip().split(" "))
ns = list(map(int, sys.stdin.readline().strip().split(" ")))
solution()
if changed:
    print(ans)
else:
    print(0)
