import sys


def solve():
    global board, calls_list, coords

    bingo = 0
    answer = 0

    for calls in calls_list:
        for c in calls:
            answer += 1
            x, y = coords[c]
            visited[x][y] = True
            bingo += check(x, y)
            if bingo >= 3:
                return print(answer)



def check(x, y):
    global visited

    bingo_line = 0

    is_one_bingo = True
    # 가로 확인
    for i in range(5):
        if not visited[x][i]:
            is_one_bingo = False
            break
    if is_one_bingo:
        bingo_line += 1

    is_one_bingo = True
    # 세로 확인
    for i in range(5):
        if not visited[i][y]:
            is_one_bingo = False
            break
    if is_one_bingo:
        bingo_line += 1

    is_one_bingo = True
    # 우하향 대각선
    if x == y:
        for i in range(5):
            if not visited[i][i]:
                is_one_bingo = False
                break
        if is_one_bingo:
            bingo_line += 1

    is_one_bingo = True
    # 좌하향 대각선
    if x+y == 4:
        for i in range(5):
            if not visited[i][4-i]:
                is_one_bingo = False
                break

        if is_one_bingo:
            bingo_line += 1

    return bingo_line


board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

coords = {}
for i in range(5):
    for j in range(5):
        coords[board[i][j]] = (i, j)

calls_list = []
for _ in range(5):
    calls_list.append(list(map(int, sys.stdin.readline().strip().split(" "))))

visited = [[False for _ in range(5)] for _ in range(5)]
solve()