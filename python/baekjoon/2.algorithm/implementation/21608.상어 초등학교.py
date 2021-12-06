import sys


def solve():
    global infos, board

    for num in orders:
        x, y = get_position(infos[num])
        board[x][y] = num

    print(cal_grade())


def get_position(prior_info):
    global board, n, ds

    cx, cy = -1, -1
    cur_prior_cnt, cur_empty_cnt = -1, -1

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                continue

            prior_cnt, empty_cnt = get_prior_empty_cnt(i, j, prior_info)

            if prior_cnt < cur_prior_cnt:
                continue

            elif prior_cnt > cur_prior_cnt:
                cur_prior_cnt, cur_empty_cnt, cx, cy = prior_cnt, empty_cnt, i, j

            else:
                if empty_cnt < cur_empty_cnt:
                    continue

                elif empty_cnt > cur_empty_cnt:
                    cur_empty_cnt, cx, cy = empty_cnt, i, j

                else:
                    if i > cx:
                        continue

                    elif i < cx:
                        cx, cy = i, j

                    else:
                        if cy > j:
                            continue

                        elif j < cy:
                            cy = j

    return cx, cy


def get_prior_empty_cnt(x, y, prior_info):
    global board, n, ds

    prior_cnt, empty_cnt = 0, 0

    for dx, dy in ds:
        nx, ny = x+dx, y+dy

        if not valid(nx, ny):
            continue

        if board[nx][ny] == 0:
            empty_cnt += 1

        else:
            if board[nx][ny] in prior_info:
                prior_cnt += 1

    return prior_cnt, empty_cnt


def valid(x, y):
    global n

    return 0 <= x < n and 0 <= y < n


def cal_grade():
    global n, board

    prior_score_map = {
        0: 0,
        1: 1,
        2: 10,
        3: 100,
        4: 1000
    }

    result = 0
    for i in range(n):
        for j in range(n):
            result += prior_score_map[get_prior_neighbor_cnt(i, j)]

    return result


def get_prior_neighbor_cnt(x, y):
    global board, n, ds, infos

    cnt = 0
    for dx, dy in ds:
        nx, ny = x+dx, y+dy

        if not valid(nx, ny):
            continue

        if board[nx][ny] in infos[board[x][y]]:
            cnt += 1

    return cnt


ds = ((-1, 0), (1, 0), (0, -1), (0, 1))
n = int(sys.stdin.readline().strip())
board = [[0 for _ in range(n)] for _ in range(n)]
infos = {}
orders = []
for _ in range(n*n):
    num, p1, p2, p3, p4 = map(int, sys.stdin.readline().strip().split(" "))
    infos[num] = {p1, p2, p3, p4}
    orders.append(num)

solve()