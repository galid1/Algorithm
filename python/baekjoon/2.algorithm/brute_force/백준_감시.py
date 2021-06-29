import sys


def find_cctvs():
    global n, m, office, cctvs

    for i in range(n):
        for j in range(m):
            if 1 <= office[i][j] <= 5:
                cctvs.append((i, j, office[i][j]))


def dfs(cctv_idx, cmds):
    global n, m, office, ds, min_ans, cctvs

    # 모든 시시티비 배치를 완료한 경우
    if len(cmds) == len(cctvs):
        ans = 0
        v = [[0 for _ in range(m)] for _ in range(n)]

        for k in range(len(cmds)):
            for c in cmds[k]:
                x, y = cctvs[k][0], cctvs[k][1]
                new_x, new_y = (x + dx[c], y + dy[c])
                while True:
                    if 0 <= new_x < n and 0 <= new_y < m and office[new_x][new_y] != 6:
                        v[new_x][new_y] = 1
                        new_x, new_y = (new_x + dx[c], new_y + dy[c])
                    else:
                        break

        for i in range(n):
            for j in range(m):
                if office[i][j] == 0 and not v[i][j]:
                    ans += 1

        min_ans = min(min_ans, ans)
        return

    # dfs
    for d in ds[cctvs[cctv_idx][2]]:
        cmds.append(d)
        dfs(cctv_idx+1, cmds)
        cmds.pop()



min_ans = 100
# 상 0 하 1 좌 2 우 3
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ds = {
    1: [[0], [1], [2], [3]],
    2: [[2, 3], [0, 1]],
    3: [[0, 3], [3, 1], [1, 2], [2, 0]],
    4: [[2, 3, 0], [0, 1, 3], [3, 1, 2], [1, 2, 0]],
    5: [[0, 1, 2, 3]]
}
n, m = map(int, sys.stdin.readline().strip().split(" "))
office = []
for i in range(n):
    office.append(list(map(int, sys.stdin.readline().strip().split(" "))))
cctvs = []
find_cctvs()
dfs(0, [])
print(min_ans)