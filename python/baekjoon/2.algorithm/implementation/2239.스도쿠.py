import sys

def init_visited():
    global board, vr, vc, vs

    # 행 방문 추가
    for row in range(9):
        for col in range(9):
            if board[row][col] != '0':
                vr[row].add(board[row][col])
    # 열 방문 추가
    for col in range(9):
        for row in range(9):
            if board[row][col] != '0':
                vc[col].add(board[row][col])

    # 사각형 방문 추가
    for row in range(9):
        for col in range(9):
            if board[row][col] != '0':
                vs[get_si(row, col)].add(board[row][col])


def solve(si, sj):
    global board

    if si == 9:
        return True

    ci, cj = si, sj

    while ci < 9:
        if board[ci][cj] != '0':
            ci, cj = get_next(ci, cj)
            if ci == 9:
                return True
            continue

        for num in range(1, 10):
            str_num = str(num)

            if not available(str_num, ci, cj):
                continue

            board[ci][cj] = str_num
            add_visit(str_num, ci, cj)
            ni, nj = get_next(ci, cj)

            res = solve(ni, nj)

            if res:
                return True

            board[ci][cj] = '0'
            remove_visit(str_num, ci, cj)

        return False


def get_si(i, j):
    sr, sc = i // 3, j // 3
    return sr * 3 + sc


def add_visit(num, i, j):
    global vr, vc, vs

    vr[i].add(num)
    vc[j].add(num)
    vs[get_si(i, j)].add(num)


def remove_visit(num, i, j):
    global vr, vc, vs

    vr[i].remove(num)
    vc[j].remove(num)
    vs[get_si(i, j)].remove(num)


def available(num, i, j):
    global vr, vc, vs

    if num in vr[i]:
        return False
    if num in vc[j]:
        return False
    if num in vs[get_si(i, j)]:
        return False

    return True


def get_next(i, j):
    if j + 1 == 9:
        return i+1, 0
    else:
        return i, j+1


board = []
for _ in range(9):
    board.append(list(sys.stdin.readline().strip()))

vr = [set() for _ in range(9)]
vc = [set() for _ in range(9)]
vs = [set() for _ in range(9)]
init_visited()

solve(0, 0)

for b in board:
    print(''.join(b))
