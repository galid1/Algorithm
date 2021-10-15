import sys


def solve():
    global n, l, board

    ans = 0

    for i in range(n):
        cnt, ch = 0, board[i][0]
        j = -1
        can = True
        while j < n-1:
            j += 1

            if board[i][j] == ch:
                cnt += 1
                continue

            if abs(board[i][j] - ch) >= 2:
                can = False
                break

            # 오르막
            if board[i][j] - ch == 1:
                if cnt < l:
                    can = False
                    break
                cnt, ch = 1, board[i][j]
                continue

            # 내리막
            if ch - board[i][j] == 1:

                if j+l-1 >= n:
                    can = False
                    break

                cnt, ch = 0, board[i][j]

                for k in range(j, j+l):
                    if ch != board[i][k]:
                        can = False
                        break
                j = j + l - 1

        if can:
            ans += 1


    for i in range(n):
        cnt, ch = 0, board[0][i]
        j = -1
        can = True

        while j < n-1:
            j += 1

            if board[j][i] == ch:
                cnt += 1
                continue

            if abs(board[j][i] - ch) >= 2:
                can = False
                break

            # 오르막
            if board[j][i] - ch == 1:
                if cnt < l:
                    can = False
                    break
                cnt, ch = 1, board[j][i]
                continue

            # 내리막
            if ch - board[j][i] == 1:

                if j+l-1 >= n:
                    can = False
                    break

                cnt, ch = 0, board[j][i]

                for k in range(j, j+l):
                    if ch != board[k][i]:
                        can = False
                        break
                j = j + l - 1

        if can:
            ans += 1

    print(ans)


n, l = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()

# 6 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1

# 6 2
# 3 3 2 2 1 1
# 3 3 2 2 1 1
# 3 3 2 2 1 1
# 3 3 2 2 1 1
# 3 3 2 2 1 1
# 3 3 2 2 1 1
