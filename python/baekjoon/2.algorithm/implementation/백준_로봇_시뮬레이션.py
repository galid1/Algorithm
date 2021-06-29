import sys


def valid(x, y):
    global a, b

    return 0 <= x < a and 0 <= y < b


# 입략 a=x, b=y
b, a = map(int, sys.stdin.readline().strip().split(" "))
board = [[-1 for _ in range(b)] for _ in range(a)]
# 동 남 서 북 시계방향이지만, board의 세로 축이 반대이기 때문에, N, S가 반대
ds = [[0, 1], [-1, 0], [0, -1], [1, 0]]

n, m = map(int, sys.stdin.readline().strip().split(" "))
robot_position_map = {i:[] for i in range(1, n+1)}

for robot_idx in range(1, n+1):
    y, x, direction = sys.stdin.readline().strip().split(" ")
    x, y = int(x)-1, int(y)-1

    if direction == "E":
        direction = 0
    elif direction == "S":
        direction = 1
    elif direction == "W":
        direction = 2
    elif direction == "N":
        direction = 3
                    #로봇번호,     방향
    board[x][y] = [robot_idx, direction]
    robot_position_map[robot_idx] = [x, y]

for _ in range(m):
    robot_idx, cmd, repeat = sys.stdin.readline().strip().split(" ")
    robot_idx, repeat = int(robot_idx), int(repeat)

    rx, ry = robot_position_map[robot_idx]
    robot_direction = board[rx][ry][1]
    if cmd == "F":
        dx, dy = ds[robot_direction]
        for _ in range(repeat):
            nx, ny = rx+dx, ry+dy

            # 벽 확인
            if not valid(nx, ny):
                print("Robot %d crashes into the wall" %(robot_idx))
                exit()

            if board[nx][ny] != -1:
                print("Robot %d crashes into robot %d" %(robot_idx, board[nx][ny][0]))
                exit()

            board[rx][ry] = -1
            rx, ry = nx, ny

        board[rx][ry] = [robot_idx, robot_direction]
        robot_position_map[robot_idx] = [rx, ry]

    elif cmd == "L" or cmd == "R":
        turn_cnt = repeat%4
        robot_n_direction = 0
        if cmd == "L":
            robot_n_direction = (robot_direction - turn_cnt)%4
        elif cmd == "R":
            robot_n_direction = (robot_direction + turn_cnt)%4
        board[rx][ry] = [robot_idx, robot_n_direction]

# 모두 통과
print("OK")


# output ex
# Robot X crashes into the wall: X번 로봇이 벽에 충돌하는 경우이다. 즉, 주어진 땅의 밖으로 벗어나는 경우가 된다.
# Robot X crashes into robot Y: X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우이다.



# 3 4
# 2 4
# 1 2 S
# 3 4 S
# 1 L 2
# 1 F 2
# 1 R 1
# 1 F 10


