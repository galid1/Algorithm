import sys


def solve():
    global n, g

    terminal_vertex = find_longest_terminal()
    ans = 0

    visited = [False for _ in range(n+1)]
    visited[terminal_vertex] = True
    stack = [(terminal_vertex, 0)]

    while stack:
        cur_vertex, cd = stack.pop()

        pushed = False
        for l_vertex, l_value in g[cur_vertex]:
            if not visited[l_vertex]:
                visited[l_vertex] = True
                stack.append((l_vertex, cd + l_value))
                pushed = True

        # 단말 노드 도착
        if not pushed:
            ans = max(ans, cd)

    print(ans)




def find_longest_terminal():
    global n, g

    visited = [False for _ in range(n+1)]
    stack = [(1, 0)]
    visited[1] = True

    max_d = 0
    max_vertex = 1

    while stack:
        cur_vertex, diameter = stack.pop()

        pushed = False
        for link, v in g[cur_vertex]:
            if not visited[link]:
                visited[link] = True
                pushed = True
                stack.append((link, diameter + v))

        if not pushed:
            if diameter > max_d:
                max_d = diameter
                max_vertex = cur_vertex

    return max_vertex



n = int(sys.stdin.readline().strip())
g = {i: [] for i in range(1, n + 1)}
for _ in range(n-1):
    f, t, v = map(int, sys.stdin.readline().strip().split(" "))
    g[f].append((t, v))
    g[t].append((f, v))

solve()
