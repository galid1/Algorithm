import sys


def select_position(x, y, cur, cnt):
    global n, land, ans

    # 식물 모두 심음
    if cnt == 3:
        cost = cal_cost(cur)
        ans = min(ans, cost)
        return

    while x < n:
        if valid(x, y):
            cur.append((x, y))
            plant(x, y)
            select_position(x, y, cur, cnt+1)
            pull(x, y)
            cur.pop()

        if y + 1 == n:
            x, y = x+1, 0
        else:
            y += 1


def plant(x, y):
    global land, ds

    land[x][y] = True
    for dx, dy in ds:
        nx, ny = x+dx, y+dy
        land[nx][ny] = True


def pull(x, y):
    global land

    land[x][y] = False
    for dx, dy in ds:
        nx, ny = x+dx, y+dy
        land[nx][ny] = False


def valid(x, y):
    global ds, land, n

    is_valid = True
    for dx, dy in ds:
        nx, ny = x+dx, y+dy

        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            is_valid = False
            break

        if land[nx][ny]:
            is_valid = False
            break

    return is_valid


def cal_cost(plants):
    global board

    cost = 0
    for px, py in plants:
        cost += board[px][py]
        for dx, dy in ds:
            nx, ny = px+dx, py+dy
            cost += board[nx][ny]

    return cost


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

land = [[False for _ in range(n)] for _ in range(n)]
ans = sys.maxsize
select_position(0, 0, [], 0)
print(ans)