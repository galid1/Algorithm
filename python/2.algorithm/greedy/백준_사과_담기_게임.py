import sys


def solve():
    global n, m, ps

    cur = 1
    ans = 0

    for p in ps:
        # 바구니 범위
        s, e = cur, cur + m - 1

        # 현재 바구니 범위에 들어옴
        if s <= p <= e:
            continue

        # 오른쪽으로 가야댐
        if p > e:
            ans += p-e
            cur += p-e
            continue

        if s > p:
            ans += s-p
            cur -= s-p

    print(ans)

n, m = map(int, sys.stdin.readline().strip().split(" "))
c = int(sys.stdin.readline().strip())
ps = []
for _ in range(c):
    ps.append(int(sys.stdin.readline().strip()))
solve()