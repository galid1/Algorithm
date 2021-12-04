import sys


def solve():
    global n, m, sn, d_map

    clock_result_map = get_result_maps()
    r_clock_result_map = get_result_maps(clock=False)

    ans = 0
    for i in range(1, sn + 1):
        ans += min(clock_result_map[i], r_clock_result_map[i])
    print(ans)


def get_result_maps(clock=True):
    global start_position, ss, sn, sx, sy, cds, rcds, d_map

    result_map = {i: 0 for i in range(1, sn + 1)}

    # 시작 방향
    dn = d_map[start_position][0] if clock else d_map[start_position][1]

    distance = 0
    cx, cy = sx, sy
    clear = False
    while True:
        dx, dy = cds[dn] if clock else rcds[dn]
        while True:
            nx, ny = cx + dx, cy + dy
            if not valid(nx, ny):
                break
            if nx == sx and ny == sy:
                clear = True
                break

            distance += 1
            if ss[nx][ny] >= 1:
                store_num = ss[nx][ny]
                result_map[store_num] = distance
            cx, cy = nx, ny

        if clear:
            break
        dn = (dn + 1) % 4

    return result_map


def valid(x, y):
    global n, m
    return 0 <= x <= n and 0 <= y <= m


m, n = map(int, sys.stdin.readline().strip().split(" "))
sn = int(sys.stdin.readline().strip())
ss = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, sn + 1):
    # 1 북 2 남 3 서 4 동
    x, y = map(int, sys.stdin.readline().strip().split(" "))

    if x == 1:
        ss[0][y] = i
    elif x == 2:
        ss[n][y] = i
    elif x == 3:
        ss[y][0] = i
    elif x == 4:
        ss[y][m] = i

x, y = map(int, sys.stdin.readline().strip().split(" "))
start_position = x
sx, sy = 0, 0
if x == 1:
    sx, sy = 0, y
elif x == 2:
    sx, sy = n, y
elif x == 3:
    sx, sy = y, 0
elif x == 4:
    sx, sy = y, m

#      동       남        서        북
cds = ((0, 1), (1, 0), (0, -1), (-1, 0))
#      동       북       서         남
rcds = ((0, 1), (-1, 0), (0, -1), (1, 0))
d_map = {
    1: (0, 2),
    2: (2, 0),
    3: (3, 3),
    4: (1, 1)
}
solve()