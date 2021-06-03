import sys
from collections import deque


def solve(sx, sy, clear_cnt):
    global ds, board, fuel, n, dests

    if clear_cnt == m:
        print(fuel)
        exit()

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = True

    customers = []
    find = False
    if board[sx][sy] == 2:
        customers.append((sx, sy))
        find = True

    using_fuel = 0
    q = deque([(sx, sy)])
    while q and not find:
        using_fuel += 1

        for _ in range(len(q)):
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not is_valid(nx, ny, visited):
                    continue

                if board[nx][ny] == 2:
                    find = True
                    customers.append((nx, ny))
                    break

                q.append((nx, ny))
                visited[nx][ny] = True

    if not find or using_fuel > fuel:
        print(-1)
        exit()

    # 가장 가까운 승객 반환
    nsx, nsy = find_near_customer(customers)
    board[nsx][nsy] = 0

    fuel -= using_fuel

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[nsx][nsy] = True

    using_fuel = 0
    q = deque([(nsx, nsy)])
    dsx, dsy = dests[(nsx, nsy)]
    find = False

    while q and not find:
        using_fuel += 1

        for _ in range(len(q)):
            cx, cy = q.popleft()

            for dx, dy in ds:
                nx, ny = cx+dx, cy+dy

                if not is_valid(nx, ny, visited):
                    continue

                if nx == dsx and ny == dsy:
                    find = True
                    break

                visited[nx][ny] = True
                q.append((nx, ny))

            if find:
                break

    if using_fuel > fuel:
        print(-1)
        exit()

    fuel += using_fuel
    solve(dsx, dsy, clear_cnt + 1)


# customers의 거리는 일단 동일, 행, 열이 작은 것 반환
def find_near_customer(customers):
    nx, ny = 21, 21
    for x, y in customers:
        if nx > x:
            nx, ny = x, y
            continue
        if nx == x and ny > y:
            nx, ny = x, y

    return nx, ny


def is_valid(x, y, visited):
    global n, board

    return 0 <= x < n and 0 <= y < n and not visited[x][y] and board[x][y] != 1




ds = [(-1, 0), (0, -1), (0, 1), (1, 0)]
n, m, fuel = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

sx, sy = map(int, sys.stdin.readline().strip().split(" "))
sx, sy = sx - 1, sy - 1
dests = {}
for _ in range(m):
    stx, sty, destx, desty = map(int, sys.stdin.readline().strip().split(" "))
    stx, sty, destx, desty = stx - 1, sty - 1, destx - 1, desty - 1
    board[stx][sty] = 2
    dests[(stx, sty)] = (destx, desty)
solve(sx, sy, 0)

# 6 3 15
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 6 5
# 2 2 5 4
# 5 4 1 6
# 1 6 3 5