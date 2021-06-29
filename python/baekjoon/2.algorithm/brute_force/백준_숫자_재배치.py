import sys

def solution(idx, cur):
    global al, b, ans, visited

    if len(cur) == len(al):
        if int(cur) <= b:
            ans = max(ans, int(cur))
        return

    for i in range(len(al)):
        if idx == 0 and al[i] == '0':
            continue

        if not visited[i]:
            visited[i] = True
            cur += al[i]
            solution(idx + 1, cur)
            cur = cur[:-1]
            visited[i] = False


a, b = map(int, sys.stdin.readline().strip().split(" "))
al = list(str(a))
ans = -1
visited = [False for _ in range(len(al))]
solution(0, '')
print(ans)