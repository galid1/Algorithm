import sys

def solve(cur):
    global n, visited

    if len(cur) == n:
        for c in cur:
            print(c, end=' ')
        print()
        return

    for i in range(1, n+1):
        if not visited[i]:
            cur.append(i)
            visited[i] = True
            solve(cur)
            visited[i] = False
            cur.pop()



n = int(sys.stdin.readline().strip())
visited = [False for _ in range(n+1)]
solve([])