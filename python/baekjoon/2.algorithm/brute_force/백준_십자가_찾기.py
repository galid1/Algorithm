import sys
from collections import deque


def solution():
    global n, m, board

    ans = []
    covered = [[True for _ in range(m)] for _ in range(n)]
    mark_asterisk(board, covered)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '*':
                size = cover_and_cal_size(board, (i, j), covered)
                if size > 0:
                    ans.append((i+1, j+1, size))

    if not answerable(covered):
        print(-1)
    else:
        print(len(ans))
        print_ans(ans)


def rollback_mark(covered, undo_log, asterisks):
    for i in range(len(asterisks)):
        x, y = asterisks[i]
        covered[x][y] = undo_log[i]


def cover_and_cal_size(board, center_coord, covered):
    q = deque()
    # 상, 하, 좌, 우
    q.append([center_coord, center_coord, center_coord, center_coord])
    res = 0

    while q:
        cur = q.popleft()
        next_coord = []
        # 만약 십자가가 아닌 경우 마크한것을 되돌리기 위해 이전 상태를 기록하는 곳
        undo_log = []

        for i in range(4):
            cx, cy = cur[i]

            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == '*':
                next_coord.append((nx, ny))
                undo_log.append(covered[nx][ny])
                covered[nx][ny] = True

        if len(next_coord) == 4:
            covered[center_coord[0]][center_coord[1]] = True
            res += 1
            q.append(next_coord)
        else:
            rollback_mark(covered, undo_log, next_coord)
            return res

    return res



def mark_asterisk(board, covered):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '*':
                covered[i][j] = False


def print_ans(ans):
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=' ')
        print()


def answerable(visit):
    res = True
    for i in range(len(visit)):
        for j in range(len(visit[0])):
            if not visit[i][j]:
                res = False
    return res


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))

solution()
