import sys, copy
from collections import deque


def choice(archers, idx):
    global n, m, d, board

    if len(archers) == 3:
        attack(archers)
        return

    for i in range(idx, m):
        archers.append((n, i))
        choice(archers, i+1)
        archers.pop()



def attack(archers):
    global n, m, d, board, ans

    t_board = copy.deepcopy(board)

    kill = 0
    # 세로 길이만큼 진행
    for i in range(n):
        will_died = []
        # 공격
        for ax, ay in archers:
            q = deque([(ax, ay)])
            cd = 0
            visited = [[False for _ in range(m)] for _ in range(n)]
            found_enemy = False
            while q:
                # 현재 사정거리 증가, 사정거리 확인
                cd += 1
                if cd > d:
                    break

                for _ in range(len(q)):
                    cx, cy = q.popleft()
                    # 좌, 상, 우 순으로 탐색
                    for dx, dy in ds:
                        nx, ny = cx+dx, cy+dy

                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            if t_board[nx][ny] == 1:
                                found_enemy = True
                                will_died.append((nx, ny))
                                break

                            q.append((nx, ny))
                            visited[nx][ny] = True

                    if found_enemy:
                        break

                if found_enemy:
                    break

        # 적 없애기
        for kx, ky in will_died:
            if t_board[kx][ky] == 1:
                kill += 1
                t_board[kx][ky] = 0

        # 적 이동
        move_enemy(t_board)

    ans = max(ans, kill)


def move_enemy(board):
    board.pop()
    board.appendleft([0 for _ in range(m)])


# 좌, 상, 우
ds = ((0, -1), (-1, 0), (0, 1))
n, m, d = map(int, sys.stdin.readline().strip().split(" "))
board = deque([])
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ans = 0
choice([], 0)
print(ans)

# 5 5 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 1 1 1 1

# 10 10 8
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# => 30

# 5 5 3
# 1 1 1 0 1
# 0 1 1 0 0
# 1 1 1 0 0
# 0 1 1 0 0
# 1 1 1 0 0
# => 13