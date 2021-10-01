import sys

def solve(remain, chosen, si):
    global n, board

    if len(chosen) == n//2:
        update_min_diff(chosen, remain)
        return

    for i in range(si, n):
        remain.remove(i)
        chosen.append(i)
        solve(remain, chosen, i+1)
        chosen.pop()
        remain.add(i)


def update_min_diff(chosen, remain):
    global ans, board

    start_res, link_res = 0, 0

    for a in chosen:
        for b in chosen:
            if a == b:
                continue
            start_res += board[a][b]

    for a in remain:
        for b in remain:
            if a == b:
                continue
            link_res += board[a][b]

    ans = min(ans, abs(start_res - link_res))


n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ans = 100000
solve(set([i for i in range(n)]), [], 0)
print(ans)