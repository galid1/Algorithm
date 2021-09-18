import sys


def solve(idx, sums):
    global ans, players, visited

    if idx == 11:
        ans = max(ans, sums)
        return

    selected_position_cnt = 0
    for i in range(11):
        if players[idx][i] == 0:
            continue

        if visited[i]:
            continue

        visited[i] = True
        solve(idx+1, sums + players[idx][i])
        visited[i] = False

        if selected_position_cnt >= 5:
            return



t = int(sys.stdin.readline().strip())
visited = [False for _ in range(11)]
for _ in range(t):
    players = []
    for _ in range(11):
        players.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    ans = 0
    solve(0, 0)
    print(ans)