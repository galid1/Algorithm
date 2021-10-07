import sys


def solve():
    global n, m, board, ts

    max_result = 0
    for (xl, yl) in ts.keys():
        for mino in ts[(xl, yl)]:
            for i in range(n - xl + 1):
                for j in range(m - yl + 1):
                    max_result = max(max_result, get_cur_size(i, j, mino))

    print(max_result)


def get_cur_size(i, j, mino):
    global board

    result = 0
    for x, y in mino:
        result += board[i+x][j+y]

    return result


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ts = {
    (2, 2): [
        [[0, 0], [0, 1], [1, 0], [1, 1]]
    ],

    (1, 4): [
        [[0, 0], [0, 1], [0, 2], [0, 3]]
    ],

    (4, 1): [
        [[0, 0], [1, 0], [2, 0], [3, 0]]
    ],

    (2, 3): [
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 1], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [0, 1], [0, 2], [1, 0]],
        [[0, 0], [1, 0], [1, 1], [1, 2]],
        [[0, 2], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 1], [0, 2], [1, 0], [1, 1]],
        [[0, 0], [0, 1], [1, 1], [1, 2]]
    ],

    (3, 2): [
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 1], [1, 1], [2, 0], [2, 1]],
        [[0, 1], [1, 0], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [1, 0], [2, 0]],
        [[0, 0], [1, 0], [1, 1], [2, 0]],
        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 1], [1, 0], [1, 1], [2, 0]]
    ]
}

solve()