import sys
from itertools import combinations


def solve():
    global empties, ans

    empty_coords = list(combinations(empties, 3))

    for coords in empty_coords:
        arrange(coords)
        if can_hide():
            ans = 'YES'
            return
        de_arrange(coords)


def can_hide():
    global board, teachers, ds

    def valid(x, y):
        global n
        return 0 <= x < n and 0 <= y < n

    for tx, ty in teachers:
        for dx, dy in ds:
            nx, ny = tx, ty

            while True:
                nx, ny = nx+dx, ny+dy

                if not valid(nx, ny):
                    break

                if board[nx][ny] == 'O' or board[nx][ny] == 'T':
                    break

                if board[nx][ny] == 'S':
                    return False

    return True


def arrange(coords):
    global board
    for x, y in coords:
        board[x][y] = 'O'


def de_arrange(coords):
    global board
    for x, y in coords:
        board[x][y] = 'X'


def find_points():
    global board, n, teachers, empties

    teachers = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                teachers.append([i, j])
            elif board[i][j] == 'X':
                empties.append([i, j])

    return teachers


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip().split(' ')))

teachers = []
empties = []
find_points()
ans = "NO"
solve()
print(ans)


# 5
# X X X X X
# X X X X X
# X X T X X
# X X X X X
# X X X S X