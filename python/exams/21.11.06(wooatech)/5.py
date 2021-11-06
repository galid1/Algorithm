def solution(rows, columns):
    visited = set()
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    board[0][0] = 1

    cr, cc = 0, 0
    remain = (rows * columns) - 1
    visited.add((0, 0, remain))
    num = 1

    repeated = False
    while remain:
        cr, cc = get_next_position(rows, columns, cr, cc, num)

        num += 1
        if (cr, cc, remain) in visited:
            repeated = True
            break

        if board[cr][cc] == 0:
            remain -= 1
        board[cr][cc] = num
        visited.add((cr, cc, remain))

    if repeated:
        for i in range(rows):
            board[i] = list(map(lambda num: num - (len(visited)//2 + 1) if num != 0 else 0, board[i]))
        board[cr][cc] = num//2

    return board


def get_next_position(rows, columns, r, c, recently_num):
    if recently_num %2 == 0:
        return (r+1) % rows, c
    else:
        return r, (c+1) % columns


# print(solution(3, 4))
# print(solution(2, 2))
# print(solution(3, 3))
# print(solution(5, 5))