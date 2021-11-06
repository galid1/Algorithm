import sys
from collections import deque


def solve():
    global n, m, fuel, sx, sy

    fail = False
    remain_customer = m
    cx, cy = sx, sy

    while not fail and remain_customer:
        result = find_customer(cx, cy, fuel)

        # 승객 태우러 가는 중 실패
        if result == -1:
            return print(-1)

        # 위치 갱신, 연료 사용, 태운 승객 제거, 승객 수 감소
        start_x, start_y, dest_x, dest_y, use_fuel = result
        fuel -= use_fuel
        board[start_x][start_y] = 0
        remain_customer -= 1

        # 목적지 이동
        use_fuel = move_to(start_x, start_y, dest_x, dest_y, fuel)

        # 목적지 이동 중 실패
        if use_fuel == -1:
            return print(-1)

        # 위치 갱신, 연료 사용 및 추가
        fuel += use_fuel
        cx, cy = dest_x, dest_y

    print(fuel)


def find_customer(sx, sy, fuel):
    global board, ds, visited, v_idx

    use_fuel = 0
    if type(board[sx][sy]) == list:
        dest_x, dest_y = board[sx][sy]
        return sx, sy, dest_x, dest_y, use_fuel

    v_idx += 1
    q = deque([[sx, sy]])
    visited[sx][sy] = v_idx
    candidates = []
    while q:
        use_fuel += 1
        # 실패
        if use_fuel >= fuel:
            return -1

        for _ in range(len(q)):
            cx, cy = q.popleft()
            for dx, dy in ds:
                nx, ny = cx + dx, cy + dy
                if not valid(nx, ny):
                    continue

                if visited[nx][ny] == v_idx:
                    continue

                if board[nx][ny] == 1:
                    continue

                if type(board[nx][ny]) == list:
                    candidates.append([nx, ny])
                    continue

                visited[nx][ny] = v_idx
                q.append([nx, ny])

        if candidates:
            break

    if not candidates:
        return -1

    candidates.sort(key=lambda position: (position[0], position[1]))
    start_x, start_y = candidates[0]
    dest_x, dest_y = board[start_x][start_y]
    return start_x, start_y, dest_x, dest_y, use_fuel


def move_to(start_x, start_y, dest_x, dest_y, fuel):
    global board, visited, v_idx

    use_fuel = 0
    v_idx += 1
    visited[start_x][start_y] = v_idx
    q = deque([[start_x, start_y]])

    while q:
        use_fuel += 1
        if use_fuel > fuel:
            return -1

        for _ in range(len(q)):
            cx, cy = q.popleft()
            for dx, dy in ds:
                nx, ny = cx + dx, cy + dy
                if not valid(nx, ny):
                    continue

                if board[nx][ny] == 1:
                    continue

                if visited[nx][ny] == v_idx:
                    continue

                if nx == dest_x and ny == dest_y:
                    return use_fuel

                visited[nx][ny] = v_idx
                q.append([nx, ny])

    return -1


def valid(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


n, m, fuel = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

sx, sy = map(lambda num: int(num)-1, sys.stdin.readline().strip().split(" "))

for _ in range(m):
    cx, cy, dx, dy = map(lambda num: int(num) - 1, sys.stdin.readline().strip().split(" "))
    board[cx][cy] = [dx, dy]

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0 for _ in range(n)] for _ in range(n)]
v_idx = 0
solve()