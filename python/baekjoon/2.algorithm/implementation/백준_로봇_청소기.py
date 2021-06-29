import sys


def solve():
    global n, m, cx, cy, d, ds, board

    ans = 0
    # visited = [[False for _ in range(m)] for _ in range(n)]
    answered = [[False for _ in range(m)] for _ in range(n)]

    is_off = False
    while True:
        if not answered[cx][cy]:
            answered[cx][cy] = True
            ans += 1

        # 4방향 탐색
        i = 0
        while True:
            # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            if i == 4:
                back = get_back_direction(d)
                dx, dy = ds[back]
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1:
                    cx, cy = nx, ny
                    i = 0
                elif 0 <= nx < n and 0 <= ny < m:
                    is_off = True
                    break

                continue

            nd = get_left_direction(d)
            dx, dy = ds[nd]
            nx, ny = cx + dx, cy + dy

            # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            if 0 <= nx < n and 0 <= ny < m and not answered[nx][ny] and board[nx][ny] != 1:
                d = nd
                cx, cy = nx, ny
                break

            # b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            d = nd
            i += 1

        if is_off:
            return print(ans)



def get_left_direction(d):
    return (d-1)%4


def get_back_direction(d):
    return (d+2)%4



#       북       동       남       서
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, sys.stdin.readline().strip().split(" "))
cx, cy, d = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()

# 3 4
# 1 0 2
# 0 1 1 1
# 0 0 0 1
# 0 1 1 1
