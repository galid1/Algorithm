import sys
from collections import deque


def solve():
    global board, combs

    dfs(0, [], 0)

    for c in combs:
        print(c)


def dfs(start_i, cur, cnt_y):
    global board, combs, ans

    if len(cur) == 7 and linked(cur):
        ans += 1
        return

    for i in range(start_i, len(board)):
        if board[i] == 'Y' and cnt_y + 1 >= 4:
            continue

        cur.append(i)

        next_cnt_y = cnt_y
        if board[i] == 'Y':
            next_cnt_y += 1

        dfs(i+1, cur, next_cnt_y)
        cur.pop()


def linked(combs):
    global visited, ds
    xys = [[num//5, num%5] for num in combs]

    queue = deque([xys[0]])
    visited[xys[0][0]][xys[0][1]] = True

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in ds:
            nx, ny = cx+dx, cy+dy

            if not valid(nx, ny):
                continue

            if nx*5 + ny not in combs:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append([nx, ny])

    is_linked = True
    for x, y in xys:
        if not visited[x][y]:
            is_linked = False
        visited[x][y] = False

    return is_linked



def valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5



ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
board = []
for _ in range(5):
    board.extend(list(sys.stdin.readline().strip()))

combs = []
visited = [[False for _ in range(5)] for _ in range(5)]
ans = 0
solve()
print(ans)