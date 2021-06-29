import sys


def solve():
    global board

    visited = [[[False for _ in range(4)] for _ in range(19)] for _ in range(19)]

    for i in range(19):
        for j in range(19):
            cur_stone = board[i][j]

            # 빈칸
            if cur_stone == 0:
                continue

            # 3방향 탐색
            for di in range(4):
                stone_cnt = 1
                cx, cy = i, j
                visited[cx][cy][di] = True
                while True:
                    nx, ny = cx+ds[di][0], cy+ds[di][1]

                    if not is_valid(nx, ny, di, visited, cur_stone):
                        break

                    visited[nx][ny][di] = True
                    cx, cy = nx, ny
                    stone_cnt += 1

                # 정답
                if stone_cnt == 5:
                    print(cur_stone)

                    # 세로
                    if di == 3:
                        print(cx + 1, cy + 1)
                    # 나머지
                    else:
                        print(i + 1, j + 1)
                    return

    print(0)



def is_valid(x, y, direction, visited, cur_stone):
    global board
    return 0 <= x < 19 and 0 <= y < 19 and not visited[x][y][direction] and board[x][y] == cur_stone


#       우       하     대각선    좌하 대각선
ds = [(0, 1), (1, 0), (1, 1), (1, -1)]
board = []
for _ in range(19):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()

# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
# 0 1 2 2 2 2 2 2 1 0 0 0 1 0 0 1 0 0 1
# 0 0 1 2 0 0 0 2 1 0 0 0 1 1 1 1 0 0 1
# 0 0 0 1 2 0 1 0 0 0 0 0 1 1 0 0 0 0 1
# 0 0 0 0 1 1 2 0 0 0 0 0 1 0 0 0 0 0 0
# 0 0 1 1 1 1 2 0 0 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0