import sys
from collections import deque


def solve():
    global n, board

    x, y = find_shark()
    sec = 0
    size = 2
    eaten = 0

    nx, ny = x, y
    while True:
        feeds_candidate, distance = find_feeds(nx, ny, size)

        # 끝
        if not feeds_candidate:
            return print(sec)

        # 걸린 시간 추가
        sec += distance
        # 제일 우선도 높은 먹이를 찾는다
        nx, ny = find_high_priority_feed(feeds_candidate)

        # 먹이 먹음 처리
        board[nx][ny] = 0
        eaten += 1
        if eaten == size and size < 7:
            size += 1
            eaten = 0




def find_high_priority_feed(feeds_candidate):
    global n

    rx, ry = n, n

    for cx, cy in feeds_candidate:
        # 더 위에 있음
        if rx > cx:
            rx, ry = cx, cy
            continue
        # x가 같은 경우
        elif rx == cx:
            # 더 왼쪽에 있음
            if ry > cy:
                rx, ry = cx, cy

    return (rx, ry)


def find_shark():
    global n, board

    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                return (i, j)


def find_feeds(x, y, size):
    global n, board, dx, dy
    q = deque([(x, y)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[x][y] = True

    feed_candidate = []
    distance = 0
    while q:
        if feed_candidate:
            return feed_candidate, distance

        distance += 1

        for _ in range(len(q)):
            cx, cy = q.popleft()

            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]

                if not in_boundary(nx, ny):
                    continue

                if visited[nx][ny]:
                    continue

                # 먹을 수 있음
                if board[nx][ny] != 0 and size > board[nx][ny]:
                    feed_candidate.append((nx, ny))
                    visited[nx][ny] = True
                    continue

                # 지나가기 가능
                if board[nx][ny] == 0 or size == board[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    continue

    if feed_candidate:
        return feed_candidate, distance
    return [], 0


def in_boundary(x, y):
    global n

    if 0 <= x < n and 0 <= y < n:
        return True
    return False


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve()
