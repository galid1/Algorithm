import sys


def solve():
    global n, m, k, board, ps

    shark_infos, smells = init()

    time = 0
    while time < 1000:
        next_shark_infos = {}

        for num in shark_infos.keys():
            x, y, d = shark_infos[num]

            # 방향 정보 가져오기
            nx, ny, nd = get_next_position(num, x, y, d, smells, time)
            # 이동
            move_to(num, x, y, nx, ny, nd, next_shark_infos)

        shark_infos = next_shark_infos

        # 겹친 상어 제거
        remove_sharks(shark_infos)

        # 냄새 풍기기
        time += 1
        do_smell(shark_infos, smells, time)

        if len(shark_infos.keys()) == 1:
            return print(time)

    print(-1)


def do_smell(shark_infos, smells, time):
    global k

    for num in shark_infos.keys():
        x, y, d = shark_infos[num]
        smells[x][y] = [time + k, num]


def remove_sharks(shark_infos):
    global n, board

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                min_num = min(board[i][j])
                for num in board[i][j]:
                    if num == min_num:
                        continue

                    shark_infos.pop(num)

                board[i][j] = set([min_num])


def move_to(num, bx, by, nx, ny, nd, next_shark_infos):
    global board

    # board에서 옮기기
    board[bx][by].remove(num)
    board[nx][ny].add(num)

    # 다음 상어 목록에 추가
    next_shark_infos[num] = (nx, ny, nd)


def get_next_position(num, x, y, d, smells, cur_time):
    global ps, ds

    my_smell_x, my_smell_y, my_smell_d = -1, -1, -1
    for nd in ps[num][d]:
        dx, dy = ds[nd]
        nx, ny = x+dx, y+dy

        if not valid(nx, ny):
            continue

        smell_time, smell_num = smells[nx][ny]

        # 냄새가 없음
        if cur_time >= smell_time:
            return nx, ny, nd
        else:
            if smell_num == num and my_smell_x == -1:
                my_smell_x, my_smell_y, my_smell_d = nx, ny, nd

    return my_smell_x, my_smell_y, my_smell_d


def valid(x, y):
    global n

    return 0 <= x < n and 0 <= y < n


def init():
    global board, n, init_directions, k

    smells = [[[0, -1] for _ in range(n)] for _ in range(n)]
    shark_infos = {}

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                board[i][j] = set()
            else:
                shark_num = board[i][j]
                shark_infos[shark_num] = (i, j, init_directions[shark_num])
                board[i][j] = set([shark_num])
                smells[i][j] = [k, shark_num]

    return shark_infos, smells


##### 입력
n, m, k = map(int, sys.stdin.readline().strip().split(" "))

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

init_directions = [0] + list(map(lambda item: int(item)-1, sys.stdin.readline().strip().split(" ")))

ps = {}
for num in range(1, m+1):
    ps[num] = []
    for _ in range(4):
        ps[num].append(list(map(lambda item: int(item)-1, sys.stdin.readline().strip().split(" "))))

ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

solve()
