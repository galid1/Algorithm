import sys


def solve():
    global n, c, m, ps

    cs = [c for _ in range(n + 1)]
    res = 0

    for to, _from, cnt in ps:
        min_c = min(cnt, 10001)

        # 실을 수 있는 용량 찾기
        for v in range(_from, to):
            min_c = min(min_c, cs[v])

        res += min_c
        for v in range(_from, to):
            cs[v] -= min_c

    print(res)


n, c = map(int, sys.stdin.readline().strip().split(" "))
m = int(sys.stdin.readline().strip())
ps = []
for i in range(m):
    _from, to, cnt = map(int, sys.stdin.readline().strip().split(" "))
    ps.append((to, _from, cnt))
ps.sort()
solve()

# 4 40
# 6
# 3 4 20
# 1 2 10
# 1 3 20
# 1 4 30
# 2 3 10
# 2 4 20

# 4 1000
# 3
# 1 4 1000
# 2 3 30
# 3 4 50

# 4 40
# 4
# 2 3 10
# 1 4 50
# 2 4 20
# 3 4 20
