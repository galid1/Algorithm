import sys


def solve():
    global board, n, m

    can_exit = [[False for _ in range(m)] for _ in range(n)]
    can_not_exit = [[False for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # 이미 탈출 가능 경로거나, 탈출 불가능 경로
            if can_exit[i][j]:
                continue
            elif can_not_exit[i][j]:
                continue

            # 탈출 가능한지 확인
            stack = [(i, j)]
            paths = [(i, j)]

            visited[i][j] = True

            while stack:
                cx, cy = stack.pop()
                nx, ny = get_next(cx, cy)

                # 이미 판가름 난 곳
                if 0 <= nx < n and 0 <= ny < m:
                    if can_exit[nx][ny]:
                        update_exit_history(can_exit, paths)
                        break
                    elif can_not_exit[nx][ny]:
                        update_exit_history(can_not_exit, paths)
                        break

                # 탈출 했는지 확인
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    update_exit_history(can_exit, paths)
                    break
                # 탈출 불가능 한지 확인
                elif visited[nx][ny]:
                    update_exit_history(can_not_exit, paths)
                    break
                # 일반적인 경로
                else:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    paths.append((nx, ny))

    # 정답
    print_ans(can_exit, m, n)


def print_ans(can_exit, m, n):
    ans = 0
    for i in range(n):
        for j in range(m):
            if can_exit[i][j]:
                ans += 1
    print(ans)


def get_next(i, j):
    global board

    if board[i][j] == 'U':
        return (i-1, j)
    elif board[i][j] == 'D':
        return (i+1, j)
    elif board[i][j] == 'L':
        return (i, j-1)
    elif board[i][j] == 'R':
        return (i, j+1)


def update_exit_history(history, paths):
    for x, y in paths:
        history[x][y] = True


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))
solve()