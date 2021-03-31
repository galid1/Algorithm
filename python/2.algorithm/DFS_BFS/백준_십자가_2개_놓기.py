import sys
from collections import deque


def select_points(points, i, j):
    global n, m, board, ans

    if len(points) == 2:
        mark(points)
        return

    ni, nj = i, j
    while ni < n:
        if board[ni][nj] == '#':
            points.append((ni, nj))
            ni = ni + 1 if nj + 1 == m else ni
            nj = nj + 1 if nj + 1 < m else 0
            select_points(points, ni, nj)
            points.pop()
        else:
            ni = ni + 1 if nj + 1 == m else ni
            nj = nj + 1 if nj + 1 < m else 0


def mark(points):
    global board, n, m, dx, dy, ans
    visited = [[False for _ in range(m)] for _ in range(n)]
    marked_list = []

    # 1,1 1,2 1,3 ... 2,1 2,2 2,3 X -> 2,2
    # 첫번째 십자가를 위한 것
    f_c = 0
    fx, fy = points[0]
    visited[fx][fy] = True
    fq = deque()
    fq.append((fx, fy))
    fq.append((fx, fy))
    fq.append((fx, fy))
    fq.append((fx, fy))
    while f_c <= 7:
        # 두번째 십자가
        s_c = 0
        sx, sy = points[1]
        visited[sx][sy] = True
        sq = deque()
        sq.append((sx, sy))
        sq.append((sx, sy))
        sq.append((sx, sy))
        sq.append((sx, sy))
        sec_marked_list = []
        while s_c <= 7:
            ans = max(ans, cal((f_c, s_c)))

            for di in range(4):
                sx, sy = sq.popleft()
                sx, sy = sx+dx[di], sy+dy[di]
                if 0 <= sx < n and 0 <= sy < m and board[sx][sy] == '#' and not visited[sx][sy]:
                    sq.append((sx, sy))
                    visited[sx][sy] = True
                    sec_marked_list.append((sx, sy))
                else:
                    break
            # 두점에 모두 십자가를 제대로 그린 경우
            if len(sq) == 4:
                s_c += 1
            else:
                for (mx, my) in sec_marked_list:
                    visited[mx][my] = False
                break

        for di in range(4):
            fx, fy = fq.popleft()
            fx, fy = fx+dx[di], fy+dy[di]

            if 0 <= fx < n and 0 <= fy < m and board[fx][fy] == '#':
                visited[fx][fy] = True
                fq.append((fx, fy))
            else:
                return

        if len(fq) == 4:
            f_c += 1
        else:
            return

def cal(crosses):
    return get_cross_area(crosses[0]) * get_cross_area(crosses[1])


def get_cross_area(cross):
    if cross == 0:
        return 1
    return 1 + 4 * cross


# 입력
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

ans = 0
# 십자가 배치 가능한 정점 두개 선택
select_points([], 0, 0)
print(ans)
