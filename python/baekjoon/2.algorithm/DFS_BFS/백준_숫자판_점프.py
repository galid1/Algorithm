import sys

def solve():
    global board
    for i in range(5):
        for j in range(5):
            find(str(board[i][j]), i, j)


def find(cur, i, j):
    global board, dx, dy, ans

    if len(cur) >= 6:
        ans.add(cur)
        return

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if 0 <= ni < 5 and 0 <= nj < 5:
            find(cur + board[ni][nj], ni, nj)



dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
board = []
for i in range(5):
    board.append(list(sys.stdin.readline().strip().split(" ")))
ans = set()
solve()
print(len(ans))