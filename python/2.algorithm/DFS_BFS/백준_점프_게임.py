import sys

def solve():
    global n, k, board, visited

    stack = []
    stack.append((0, 0))
    visited[0][0] = True

    end_line = 0
    while stack:
        for _ in range(len(stack)):
            cx, cy = stack.pop()

            if cy + 1 >= n:
                print(1)
                return
            elif board[cx][cy+1] == 1 and not visited[cx][cy+1] and end_line < cy+1 < n:
                stack.append((cx, cy+1))
                visited[cx][cy+1] = True

            if cy - 1 >= n:
                print(1)
                return
            elif board[cx][cy-1] == 1 and not visited[cx][cy-1] and end_line < cy-1 < n:
                stack.append((cx, cy-1))
                visited[cx][cy-1] = True

            if cy + k >= n:
                print(1)
                return
            else:
                nx = cx
                if nx == 1:
                    nx = 0
                else:
                    nx = 1

                if board[nx][cy+k] == 1 and not visited[nx][cy+k] and end_line < cy+k < n:
                    stack.append((nx, cy+k))
                    visited[nx][cy+k] = True

        end_line += 1

    print(0)


# 입력
n, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(2):
    board.append(list(map(int, sys.stdin.readline().strip())))
visited = [[False for _ in range(n)] for _ in range(2)]

solve()
