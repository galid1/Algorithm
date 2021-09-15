import sys


def solve():
    global board, n, k, m

    if check():
        return print(0)

    for need_cnt in range(1, 3+1):
        arrange([], need_cnt, 0, 0, 0)

    if ans == 4:
        print(-1)
    else:
        print(ans)


def arrange(cur, need_cnt, cur_cnt, sx, sy):
    global ans

    if ans != 4:
        return

    if cur_cnt == need_cnt:
        if check():
            ans = min(ans, need_cnt)

        return

    for i in range(sx, n):
        sy = sy if sx == i else 0
        for j in range(sy, m-1):
            if not valid(i, j):
                continue

            cur.append([i, j])
            link(i, j)
            arrange(cur, need_cnt, cur_cnt+1, i, j+2)
            unlink(i, j)
            cur.pop()


def valid(x, y):
    global board

    if board[x][y] != 0:
        return False

    if y == 0:
        return board[x][y+1] == 0

    return board[x][y-1] != 1 and board[x][y+1] == 0



def check():
    global board, n, m

    for start_line in range(m):
        cur_y = start_line
        for cur_x in range(n):
            cur_y += board[cur_x][cur_y]

        if start_line != cur_y:
            return False

    return True


def link(a, b):
    global board

    board[a][b] = 1
    board[a][b+1] = -1


def unlink(a, b):
    global board
    board[a][b] = 0
    board[a][b+1] = 0


m, k, n = map(int, sys.stdin.readline().strip().split(" "))
board = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    a, b = a-1, b-1
    link(a, b)


ans = 4
solve()
