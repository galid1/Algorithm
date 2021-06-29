import sys


def solve(sv, cur_visit_cnt, dis, visited):
    global n, board, ov, ans

    if cur_visit_cnt == n:
        if board[sv][ov] > 0:
            ans = min(ans, dis + board[sv][ov])
        return

    for i in range(n):
        if visited[i] or board[sv][i] == 0:
            continue

        if dis + board[sv][i] > ans:
            continue

        visited[i] = True
        solve(i, cur_visit_cnt+1, dis + board[sv][i], visited)
        visited[i] = False



n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ans = sys.maxsize
visited = [False for _ in range(n)]
for i in range(n):
    ov = i
    visited[i] = True
    solve(i, 1, 0, visited)
print(ans)