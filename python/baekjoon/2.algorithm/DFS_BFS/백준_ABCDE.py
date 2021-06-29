import sys

def solve(cv, depth):
    global n, m, g, is_ok, ans, v

    if is_ok:
        return

    # 정답 존재
    if depth == 4:
        ans = 1
        is_ok = True
        return

    for to in g[cv]:
        if not v[to]:
            v[to] = True
            solve(to, depth+1)
            v[to] = False


n, m = map(int, sys.stdin.readline().strip().split(" "))
g = {i:[] for i in range(n)}
# 친구 관계 입력
for _ in range(m):
    f, t = map(int, sys.stdin.readline().strip().split(" "))
    g[f].append(t)
    g[t].append(f)

# 정점 돌아가며 가능한지 확인
ans = 0
is_ok = False
for i in range(n):
    if is_ok:
        break

    v = [False for _ in range(n)]
    v[i] = True
    solve(i, 0)

print(ans)
