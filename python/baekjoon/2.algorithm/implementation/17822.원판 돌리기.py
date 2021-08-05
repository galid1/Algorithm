import sys
from collections import deque


def solve():
    global n, m, t, disks, cmds, disk_sums

    for x, d, k in cmds:
        turn_disk(x, d, k)

        if not find_and_remove():
            flat()

    # 정답
    print(disk_sums)


def turn_disk(x, d, k):
    global n, m, disks

    for i in range(x, n+1, x):
        print("disk : ", i)
        for _ in range(k%m):
            # 시계
            if d == 0:
                tmp = disks[i][m-1]
                for g in range(m-1, 0, -1):
                    disks[i][g] = disks[i][g-1]
                disks[i][0] = tmp

            # 반시계
            else:
                tmp = disks[i][0]
                for g in range(0, m-1):
                    disks[i][g] = disks[i][g+1]
                disks[i][m-1] = tmp


# 인접한 수를 찾고 지움
def find_and_remove():
    global n, m, disks, disk_sums, num_cnt, ds, visited

    removed = False

    q = deque()

    # 1번 디스크 부터
    for i in range(1, n+1):
        for j in range(m):
            if visited[i][j]:
                continue

            q.append([i, j])
            cur_num = disks[i][j]
            adj_cnt = 0

            while q:
                cx, cy = q.popleft()

                for dx, dy in ds:
                    nx, ny = cx+dx, (cy+dy)%m

                    if not valid(nx, ny):
                        continue

                    if visited[nx][ny]:
                        continue

                    if cur_num == disks[nx][ny]:
                        adj_cnt += 1
                        visited[nx][ny] = True
                        q.append([nx, ny])

            print("=======")
            print('i , j : ', i , j)
            print(' cur num : ', cur_num)
            print('adj_cnt : ', adj_cnt)

            if adj_cnt <= 1:
                continue

            removed = True
            disk_sums -= (cur_num * adj_cnt)
            num_cnt -= adj_cnt

    return removed


def valid(x, y):
    global n, m
    return 1 <= x < n+1 and 0 <= y < m


def flat():
    global disk_sums, num_cnt, disks, n, m

    if disk_sums == 0:
        return

    avg = disk_sums/num_cnt

    for i in range(1, n+1):
        for j in range(m):
            if disks[i][j] > avg:
                disks[i][j] -= 1
            elif disks[i][j] < avg:
                disks[i][j] += 1


n, m, t = map(int, sys.stdin.readline().strip().split(" "))

disks = [[],]
disk_sums, num_cnt = 0, n*m
visited = [[False for _ in range(m)] for _ in range(n+1)]
for _ in range(n):
    disk = list(map(int, sys.stdin.readline().strip().split(" ")))
    disks.append(disk)
    disk_sums += sum(disk)

cmds = []
for _ in range(t):
    cmds.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
solve()

# 4 4 1
# 1 1 2 3
# 5 2 4 2
# 3 1 3 5
# 2 1 3 2
# 2 0 1


# 2 2 1
# 1 1
# 1 1
# 1 0 1


# 8 4 1
# 1 1 2 3
# 5 2 4 2
# 3 1 3 5
# 2 1 3 2
# 1 1 2 3
# 5 2 4 2
# 3 1 3 5
# 2 1 3 2
# 6 0 1