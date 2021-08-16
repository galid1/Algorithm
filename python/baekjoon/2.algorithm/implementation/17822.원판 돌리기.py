import sys
from collections import deque

def solve(disks, cmds):
    global n, m

    for idx, dir, k in cmds:
        # print("=========")
        # print("bef : ")
        # for i in range(1, n+1):
        #     for j in range(m):
        #         if disks[i][j] == DELETED:
        #             print("X", end=' ')
        #             continue
        #         print(disks[i][j], end=' ')
        #     print()
        for i in range(idx, n+1, idx):
            turn_disk(disks, i, dir, k)
        # print("=========")
        # print("after turn : ")
        # for i in range(1, n + 1):
        #     for j in range(m):
        #         if disks[i][j] == DELETED:
        #             print("X", end=' ')
        #             continue
        #         print(disks[i][j], end=' ')
        #     print()


        removed = remove_adjacent_nums(disks)

        # if removed:
        #     print("after removed")
        #     for i in range(1, n + 1):
        #         for j in range(m):
        #             if disks[i][j] == DELETED:
        #                 print("X", end=' ')
        #                 continue
        #             print(disks[i][j], end=' ')
        #         print()

        if not removed:
            flatten(disks)
            # print("after flatteen")
            # for i in range(1, n + 1):
            #     for j in range(m):
            #         if disks[i][j] == DELETED:
            #             print("X", end=' ')
            #             continue
            #         print(disks[i][j], end=' ')
            #     print()

    sums = 0
    for i in range(1, n+1):
        for j in range(m):
            if disks[i][j] == DELETED:
                continue
            sums += disks[i][j]
    print(sums)



def turn_disk(disks, disk_idx, dir, k):
    global m
    turned_disk = [0 for _ in range(m)]

    # 반시계
    if dir == 1:
        k *= -1

    for idx, num in enumerate(disks[disk_idx]):
        turned_disk[(idx+k)%m] = num

    disks[disk_idx] = turned_disk


def remove_adjacent_nums(disks):
    global n, m
    removed_num_sums = 0

    for di in range(1, n+1):
        for dj in range(m):
            if disks[di][dj] == DELETED:
                continue

            removed_num_sums += bfs(disks, di, dj)

    return removed_num_sums > 0


def bfs(disks, di, dj):
    global m, DELETED

    removed_sums = 0
    q = deque([[di, dj]])
    target = disks[di][dj]

    while q:
        cx, cy = q.popleft()

        for dx, dy in ds:
            nx, ny = cx+dx, (cy+dy)%m

            if not valid(nx, ny):
                continue

            if disks[nx][ny] == DELETED:
                continue

            if disks[nx][ny] == target:
                removed_sums += disks[nx][ny]
                disks[nx][ny] = DELETED
                q.append([nx, ny])

    return removed_sums


def valid(x, y):
    global n, m

    return 1 <= x <= n and 0 <= y < m


def flatten(disks):
    global n, m, DELETED

    sums, cnt = 0, 0

    for i in range(1, n+1):
        for j in range(m):
            if disks[i][j] == DELETED:
                continue
            sums += disks[i][j]
            cnt += 1

    if sums == 0:
        print(sums)
        exit()

    avg = sums/cnt
    for i in range(1, n+1):
        for j in range(m):
            if disks[i][j] == DELETED:
                continue

            if disks[i][j] > avg:
                disks[i][j] -= 1
            elif disks[i][j] < avg:
                disks[i][j] += 1


DELETED = -1000000000
ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m, t = map(int, sys.stdin.readline().strip().split(" "))

disks = [[]]
for _ in range(n):
    disk = list(map(int, sys.stdin.readline().strip().split(" ")))
    disks.append(disk)

cmds = []
for _ in range(t):
    idx, dir, k = list(map(int, sys.stdin.readline().strip().split(" ")))
    k = k%m

    cmds.append([idx, dir, k])

solve(disks, cmds)


# 4 4 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 0 1

# 4 4 1
# 1 1 2 3
# 5 2 4 2
# 3 1 3 5
# 2 1 3 2
# 2 0 1

# 8 4 1
# 1 1 2 3
# 5 2 4 2
# 3 1 3 5
# 2 1 3 2
# 1 1 2 3
# 5 2 4 2
# 3 1 3 5
# 2 1 3 2
# 2 0 1