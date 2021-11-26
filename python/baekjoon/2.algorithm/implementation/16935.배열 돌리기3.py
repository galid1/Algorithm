import sys
from collections import deque


def solve():
    global n, m, rs, board

    for r in rs:
        if r == 1:
            do_one()
        elif r == 2:
            do_two()
        elif r == 3:
            do_three()
        elif r == 4:
            do_four()
        elif r == 5:
            do_five()
        elif r == 6:
            do_six()

    for i in range(n):
        print(*board[i])


def do_one():
    global board, n, m

    new_board = []
    for _ in range(n):
        new_board.append(board.pop())

    board = new_board


def do_two():
    global board

    new_board = []
    for i in range(n):
        new_line = deque()
        for _ in range(m):
            new_line.append(board[i].pop())

        new_board.append(new_line)

    board = new_board


def do_three():
    global board, n, m

    new_board = []

    for _ in range(m):
        new_line = deque()
        for i in range(n-1, -1, -1):
            new_line.append(board[i].popleft())

        new_board.append(new_line)

    board = new_board
    n, m = m, n


def do_four():
    global board, n, m

    new_board = []

    for _ in range(m):
        new_line = deque()
        for i in range(n):
            new_line.append(board[i].pop())
        new_board.append(new_line)

    board = new_board
    n, m = m, n


def do_five():
    global board, n, m

    new_board = [deque() for _ in range(n)]
    one, two, three, four = divide_four_section()

    for i in range(n//2):
        for _ in range(m//2):
            new_board[i].append(four[i].popleft())

    for i in range(n//2):
        for _ in range(m//2):
            new_board[i].append(one[i].popleft())

    for i in range(n//2, n):
        for _ in range(m//2):
            new_board[i].append(three[i - n//2].popleft())

    for i in range(n//2, n):
        for _ in range(m//2):
            new_board[i].append(two[i - n//2].popleft())

    board = new_board


def do_six():
    global board, n, m

    new_board = [deque() for _ in range(n)]
    one, two, three, four = divide_four_section()

    for i in range(n//2):
        for _ in range(m//2):
            new_board[i].append(two[i].popleft())

    for i in range(n//2):
        for _ in range(m//2):
            new_board[i].append(three[i].popleft())

    for i in range(n//2, n):
        for _ in range(m//2):
            new_board[i].append(one[i - n//2].popleft())

    for i in range(n//2, n):
        for _ in range(m//2):
            new_board[i].append(four[i - n//2].popleft())

    board = new_board


def divide_four_section():
    global board

    one, two, three, four = [], [], [], []

    for i in range(n//2):
        # one
        new_one_line, new_two_line = deque(), deque()
        for _ in range(m//2):
            new_one_line.append(board[i].popleft())
        # two
        for _ in range(m//2):
            new_two_line.append(board[i].popleft())

        one.append(new_one_line)
        two.append(new_two_line)

    for i in range(n//2, n):
        # three
        new_three_line, new_four_line = deque(), deque()
        for _ in range(m // 2):
            new_four_line.append(board[i].popleft())
        # four
        for _ in range(m // 2):
            new_three_line.append(board[i].popleft())

        three.append(new_three_line)
        four.append(new_four_line)

    return one, two, three, four


n, m, r = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(deque(map(int, sys.stdin.readline().strip().split(" "))))

rs = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()