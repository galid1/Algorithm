import sys


def move(fir, sec, try_cnt, move_cnt):
    global n, m, cmds, ans

    if try_cnt == m:
        ans = min(ans, move_cnt)
        return

    if move_cnt >= ans:
        return

    need_wall = cmds[try_cnt]
    # 첫번째 문 희생
    move(sec, need_wall, try_cnt + 1, move_cnt + abs(fir - need_wall))
    # 두번째 문 희생
    move(fir, need_wall, try_cnt + 1, move_cnt + abs(sec - need_wall))


n = int(sys.stdin.readline().strip())
fir, sec = map(int, sys.stdin.readline().strip().split(" "))
m = int(sys.stdin.readline().strip())
cmds = []
for _ in range(m):
    cmds.append(int(sys.stdin.readline().strip()))

ans = sys.maxsize
move(fir, sec, 0, 0)
print(ans)